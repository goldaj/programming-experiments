"""Offline end-to-end tests for the original, data-driven adventure."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

GAME = Path(__file__).resolve().parents[1] / "python/branching-adventure-qt"
sys.path.insert(0, str(GAME))

from story_engine import GameSession, Story, StoryError, discover_endings
from play_cli import play


class AdventureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = Story.from_file(GAME / "story.json")

    def test_all_seven_endings_reachable(self):
        expected = {name for name, node in self.story.nodes.items() if node["ending"]}
        self.assertEqual(len(expected), 7)
        self.assertEqual(discover_endings(self.story), expected)

    def test_inventory_gates_and_one_time_pickups(self):
        game = GameSession(self.story)
        self.assertEqual(len(game.choices()), 3)
        game.choose(0)  # forest
        self.assertEqual(game.current, "forest")
        self.assertTrue(any(x["label"] == "Prendre la lanterne" for x in game.choices()))
        game.choose(0)
        self.assertEqual(game.items, {"lantern"})
        self.assertFalse(any(x["label"] == "Prendre la lanterne" for x in game.choices()))
        game.choose(1)  # back
        game.choose(1)  # mine
        self.assertTrue(any(x["to"] == "dark_tunnel" for x in game.choices()))
        game.choose(1)
        self.assertEqual(game.current, "dark_tunnel")

    def test_hidden_relic_requires_a_read_clue(self):
        game = GameSession(self.story)
        game.choose(0)  # forest
        game.choose(0)  # lantern
        game.choose(1)  # crossroads
        game.choose(1)  # mine
        game.choose(1)  # dark tunnel
        game.choose(0)  # rune
        game.choose(0)  # chamber
        game.choose(0)  # vault
        self.assertNotIn("relic_end", [c["to"] for c in game.choices()])
        self.assertIn("wisdom_end", [c["to"] for c in game.choices()])

    def test_save_roundtrip_and_mismatched_story(self):
        with tempfile.TemporaryDirectory() as root:
            path = Path(root) / "save.json"
            game = GameSession(self.story)
            game.choose(0)
            game.choose(0)
            game.save(path)
            other = GameSession.restore(self.story, path)
            self.assertEqual((other.current, other.items, other.history),
                             (game.current, game.items, game.history))
            payload = json.loads((GAME / "story.json").read_text(encoding="utf-8"))
            payload["title"] += " nouvelle édition"
            with self.assertRaises(StoryError):
                GameSession.restore(Story(payload), path)
            invalid = json.loads(path.read_text(encoding="utf-8"))
            invalid["current"] = {"not": "a node"}
            path.write_text(json.dumps(invalid), encoding="utf-8")
            with self.assertRaises(StoryError):
                GameSession.restore(self.story, path)

    def test_bad_graphs_fail_before_playing(self):
        source = json.loads((GAME / "story.json").read_text(encoding="utf-8"))
        source["nodes"]["crossroads"]["choices"][0]["to"] = "missing"
        with self.assertRaises(StoryError):
            Story(source)
        source = json.loads((GAME / "story.json").read_text(encoding="utf-8"))
        source["nodes"]["lost_end"]["choices"] = [{"label": "Oops", "to": "crossroads"}]
        with self.assertRaises(StoryError):
            Story(source)

    def test_terminal_playthrough_saves_real_progress(self):
        with tempfile.TemporaryDirectory() as root:
            path = Path(root) / "progress.json"
            scripted = iter(["1", "1", "1", "1", "q"])
            output = []
            play(self.story, path, fresh=True, read=lambda _: next(scripted),
                 write=output.append)
            restored = GameSession.restore(self.story, path)
            self.assertEqual(restored.current, "lost_end")
            self.assertTrue(restored.finished)
            self.assertIn("lantern", restored.items)
            self.assertTrue(any("FIN : Égaré" in text for text in output))

    def test_choice_bounds_and_endings_are_read_only(self):
        game = GameSession(self.story)
        with self.assertRaises(StoryError):
            game.choose(-1)
        with self.assertRaises(StoryError):
            game.choose(900)
        with self.assertRaises(StoryError):
            game.choose(True)


if __name__ == "__main__":
    unittest.main()
