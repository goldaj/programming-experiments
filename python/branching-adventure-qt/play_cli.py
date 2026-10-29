"""Play the full branching adventure in any terminal: no PyQt required."""
from __future__ import annotations

import argparse
from pathlib import Path

from story_engine import GameSession, Story, StoryError, discover_endings

ROOT = Path(__file__).resolve().parent


def play(story: Story, save_path: Path, *, fresh: bool = False,
         read=input, write=print) -> None:
    game = GameSession(story)
    if save_path.exists() and not fresh:
        try:
            game = GameSession.restore(story, save_path)
            write("Partie sauvegardée retrouvée.")
        except (ValueError, OSError, TypeError) as error:
            write("Sauvegarde ignorée (" + str(error) + "). Nouveau départ.")
    write("\n" + story.title + "\nCommandes : nombre pour choisir, s pour sauver, r pour recommencer, q pour quitter.")
    while True:
        scene = game.scene
        write("\n=== " + scene["title"] + " ===")
        write(scene["text"])
        write("Sac : " + (", ".join(sorted(game.items)) if game.items else "vide"))
        if game.finished:
            write("FIN : " + scene["ending"] + " | r : rejouer, q : quitter")
        else:
            options = game.choices()
            for i, option in enumerate(options, 1):
                write(str(i) + ". " + option["label"])
            if not options:
                write("Aucun choix accessible. Tapez r pour recommencer.")
        try:
            entry = read("> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            write("Partie conservée sur le disque.")
            return
        if entry == "q":
            return
        if entry == "s":
            try:
                game.save(save_path)
                write("Partie enregistrée.")
            except OSError as error:
                write("Sauvegarde impossible : " + str(error))
            continue
        if entry == "r":
            game = GameSession(story)
            try:
                game.save(save_path)
            except OSError as error:
                write("Sauvegarde impossible : " + str(error))
            continue
        if not game.finished and entry.isdecimal():
            index = int(entry) - 1
            try:
                game.choose(index)
            except StoryError:
                write("Choix invalide.")
                continue
            try:
                game.save(save_path)
            except OSError as error:
                write("Sauvegarde impossible : " + str(error))
        else:
            write("Commande inconnue.")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Aventure à embranchements, hors ligne")
    parser.add_argument("--story", type=Path, default=ROOT / "story.json")
    parser.add_argument("--save", type=Path, default=ROOT / ".adventure_save.json")
    parser.add_argument("--new", action="store_true", help="Ignore saved progress")
    parser.add_argument("--audit", action="store_true", help="List reachable endings, no gameplay")
    args = parser.parse_args(argv)
    try:
        story = Story.from_file(args.story)
        if args.audit:
            reachable = discover_endings(story)
            all_endings = {key for key, node in story.nodes.items() if node["ending"]}
            print("Fins accessibles :", len(reachable), "/", len(all_endings))
            for key in sorted(reachable):
                print("-", story.nodes[key]["ending"])
            return 0 if reachable == all_endings else 1
        play(story, args.save, fresh=args.new)
        return 0
    except (OSError, ValueError, TypeError) as error:
        parser.exit(2, "Aventure indisponible : " + str(error) + "\n")


if __name__ == "__main__":
    raise SystemExit(main())
