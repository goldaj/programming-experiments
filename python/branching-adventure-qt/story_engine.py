"""A small, deterministic, data-driven branching adventure engine.

Standard library only. No GUI, network calls, code execution, or secrets.
"""
from __future__ import annotations

from collections import deque
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile

TOKEN = re.compile(r"^[a-z][a-z0-9_]{0,47}$")
ACTIONS = ("needs", "not_items", "requires_flags", "not_flags", "gives", "takes", "sets")
STATE_VERSION = 1
MAX_STORY_BYTES = 256_000
MAX_SAVE_BYTES = 64_000


class StoryError(ValueError):
    pass


def _token(value: object, description: str) -> str:
    if not isinstance(value, str) or TOKEN.fullmatch(value) is None:
        raise StoryError("Invalid " + description)
    return value


def _tokens(value: object, description: str) -> tuple[str, ...]:
    if value is None:
        return ()
    if not isinstance(value, list) or len(value) > 32:
        raise StoryError("Invalid token list: " + description)
    values = tuple(_token(item, description) for item in value)
    if len(set(values)) != len(values):
        raise StoryError("Duplicate token: " + description)
    return values


class Story:
    def __init__(self, data: dict):
        if not isinstance(data, dict):
            raise StoryError("Story must be an object")
        self.title = data.get("title")
        self.start = _token(data.get("start"), "start")
        raw_nodes = data.get("nodes")
        if not isinstance(self.title, str) or not 1 <= len(self.title) <= 120:
            raise StoryError("Title required")
        if not isinstance(raw_nodes, dict) or not 2 <= len(raw_nodes) <= 100:
            raise StoryError("Expected 2 to 100 nodes")
        self.nodes = {}
        targets = set()
        endings = set()
        all_items = set()
        all_flags = set()
        for key, node in raw_nodes.items():
            _token(key, "node id")
            if not isinstance(node, dict):
                raise StoryError("Each node must be an object")
            title, prose = node.get("title"), node.get("text")
            ending = node.get("ending")
            if (not isinstance(title, str) or not 1 <= len(title) <= 120
                    or not isinstance(prose, str) or not 1 <= len(prose) <= 3000):
                raise StoryError("Missing title/text at " + key)
            choices = node.get("choices", [])
            if not isinstance(choices, list) or len(choices) > 12:
                raise StoryError("Invalid choices at " + key)
            if ending is not None:
                if not isinstance(ending, str) or not 1 <= len(ending) <= 80 or choices:
                    raise StoryError("Ending must be labelled and terminal at " + key)
                endings.add(key)
            elif not choices:
                raise StoryError("Non-ending has no choices: " + key)
            normalized = []
            for choice in choices:
                if not isinstance(choice, dict) or not isinstance(choice.get("label"), str):
                    raise StoryError("Missing choice label at " + key)
                label = choice["label"]
                if not 1 <= len(label) <= 180:
                    raise StoryError("Invalid choice length at " + key)
                target = _token(choice.get("to"), "choice target")
                targets.add(target)
                params = {name: _tokens(choice.get(name), name) for name in ACTIONS}
                if set(params["needs"]) & set(params["not_items"]):
                    raise StoryError("Conflicting item requirement at " + key)
                if set(params["requires_flags"]) & set(params["not_flags"]):
                    raise StoryError("Conflicting flag requirement at " + key)
                if set(params["gives"]) & set(params["takes"]):
                    raise StoryError("Cannot give and take the same item")
                all_items.update(params["needs"])
                all_items.update(params["not_items"])
                all_items.update(params["gives"])
                all_items.update(params["takes"])
                all_flags.update(params["requires_flags"])
                all_flags.update(params["not_flags"])
                all_flags.update(params["sets"])
                normalized.append({"label": label, "to": target, **params})
            self.nodes[key] = {"title": title, "text": prose, "ending": ending,
                               "choices": normalized}
        if self.start not in self.nodes or not targets <= self.nodes.keys() or not endings:
            raise StoryError("Missing start, referenced node or ending")
        self.all_items = frozenset(all_items)
        self.all_flags = frozenset(all_flags)
        canonical = json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        self.fingerprint = hashlib.sha256(canonical.encode("utf-8")).hexdigest()

    @classmethod
    def from_file(cls, path: str | Path) -> "Story":
        source = Path(path)
        if source.stat().st_size > MAX_STORY_BYTES:
            raise StoryError("Story file is too large")
        return cls(json.loads(source.read_text(encoding="utf-8")))


class GameSession:
    def __init__(self, story: Story):
        self.story = story
        self.current = story.start
        self.items: set[str] = set()
        self.flags: set[str] = set()
        self.history: list[str] = [story.start]

    @property
    def scene(self) -> dict:
        return self.story.nodes[self.current]

    @property
    def finished(self) -> bool:
        return self.scene["ending"] is not None

    def choices(self) -> list[dict]:
        if self.finished:
            return []
        available = []
        for choice in self.scene["choices"]:
            if not set(choice["needs"]) <= self.items:
                continue
            if set(choice["not_items"]) & self.items:
                continue
            if not set(choice["requires_flags"]) <= self.flags:
                continue
            if set(choice["not_flags"]) & self.flags:
                continue
            available.append(choice)
        return available

    def choose(self, choice_index: int) -> None:
        options = self.choices()
        if type(choice_index) is not int or not 0 <= choice_index < len(options):
            raise StoryError("Invalid choice")
        action = options[choice_index]
        self.items.difference_update(action["takes"])
        self.items.update(action["gives"])
        self.flags.update(action["sets"])
        self.current = action["to"]
        self.history.append(self.current)
        if len(self.history) > 500:
            self.history = self.history[-500:]

    def save(self, path: str | Path) -> None:
        destination = Path(path)
        # The caller selects the local file. Atomic replace prevents truncated saves.
        destination.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "version": STATE_VERSION, "story_sha256": self.story.fingerprint,
            "current": self.current, "items": sorted(self.items),
            "flags": sorted(self.flags), "history": self.history,
        }
        payload = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
        fd, temporary = tempfile.mkstemp(prefix=".adventure-", suffix=".tmp", dir=destination.parent)
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as handle:
                handle.write(payload)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temporary, destination)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)

    @classmethod
    def restore(cls, story: Story, path: str | Path) -> "GameSession":
        source = Path(path)
        if source.stat().st_size > MAX_SAVE_BYTES:
            raise StoryError("Save file is too large")
        data = json.loads(source.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or type(data.get("version")) is not int or data["version"] != STATE_VERSION:
            raise StoryError("Incompatible save version")
        if data.get("story_sha256") != story.fingerprint:
            raise StoryError("Save belongs to another story version")
        current, history = data.get("current"), data.get("history")
        if not isinstance(current, str) or current not in story.nodes or not isinstance(history, list) or not 1 <= len(history) <= 500:
            raise StoryError("Invalid save position")
        if history[0] != story.start or history[-1] != current or any(not isinstance(x, str) or x not in story.nodes for x in history):
            raise StoryError("Invalid save history")
        items = _tokens(data.get("items"), "saved items")
        flags = _tokens(data.get("flags"), "saved flags")
        if not set(items) <= story.all_items or not set(flags) <= story.all_flags:
            raise StoryError("Unrecognized saved items or flags")
        session = cls(story)
        session.current = current
        session.items = set(items)
        session.flags = set(flags)
        session.history = history.copy()
        return session


def discover_endings(story: Story, max_states: int = 10000) -> set[str]:
    """Explore reachable game states, including inventory and flags.

    Useful for checking that all endings are actually possible to obtain.
    Fails closed on unexpectedly large stories instead of looping forever.
    """
    if max_states < 1:
        raise ValueError("max_states must be positive")
    first = GameSession(story)
    queue = deque([first])
    seen = set()
    endings = set()
    while queue:
        game = queue.popleft()
        key = (game.current, frozenset(game.items), frozenset(game.flags))
        if key in seen:
            continue
        seen.add(key)
        if len(seen) > max_states:
            raise StoryError("Story state-space limit exceeded")
        if game.finished:
            endings.add(game.current)
            continue
        for index in range(len(game.choices())):
            clone = GameSession(story)
            clone.current = game.current
            clone.items = game.items.copy()
            clone.flags = game.flags.copy()
            clone.choose(index)
            queue.append(clone)
    return endings
