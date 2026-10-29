"""Qt interface for the branching adventure.

Launch: python play_qt.py
Requires PyQt5 only for this UI; the CLI and engine require stdlib only.
The original two-choice main.py is deliberately preserved unchanged.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from story_engine import GameSession, Story, StoryError

ROOT = Path(__file__).resolve().parent


def main(argv=None):
    parser = argparse.ArgumentParser(description="Les passages de la montagne — PyQt")
    parser.add_argument("--story", type=Path, default=ROOT / "story.json")
    parser.add_argument("--save", type=Path, default=ROOT / ".adventure_save.json")
    parser.add_argument("--new", action="store_true")
    args = parser.parse_args(argv)

    try:
        from PyQt5.QtWidgets import (
            QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
            QPushButton, QTextBrowser, QMessageBox,
        )
        from PyQt5.QtCore import Qt
    except ImportError as error:
        parser.exit(2, "PyQt5 requis pour cette interface (pip install PyQt5).\n")

    try:
        story = Story.from_file(args.story)
    except (ValueError, OSError) as error:
        parser.exit(2, "Histoire invalide : " + str(error) + "\n")

    class AdventureWindow(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle(story.title)
            self.resize(760, 540)
            self.story = story
            self.game = GameSession(story)

            layout = QVBoxLayout(self)
            self.title = QLabel()
            self.title.setStyleSheet("font-size: 20px; font-weight: bold;")
            layout.addWidget(self.title)
            self.prose = QTextBrowser()
            self.prose.setOpenExternalLinks(False)
            layout.addWidget(self.prose, 1)
            self.inventory = QLabel()
            self.inventory.setWordWrap(True)
            layout.addWidget(self.inventory)

            self.choices_layout = QVBoxLayout()
            layout.addLayout(self.choices_layout)
            actions = QHBoxLayout()
            self.restart_button = QPushButton("Nouvelle partie")
            self.restart_button.clicked.connect(self.restart)
            actions.addWidget(self.restart_button)
            self.save_button = QPushButton("Sauvegarder")
            self.save_button.clicked.connect(self.save)
            actions.addWidget(self.save_button)
            self.load_button = QPushButton("Reprendre")
            self.load_button.clicked.connect(self.load)
            actions.addWidget(self.load_button)
            layout.addLayout(actions)

            self.status = QLabel()
            self.status.setWordWrap(True)
            layout.addWidget(self.status)
            if args.save.exists() and not args.new:
                self.load()
            else:
                self.render()

        def render(self):
            node = self.game.scene
            self.title.setText(node["title"])
            self.prose.setPlainText(node["text"])
            self.inventory.setText(
                "Sac : " + (", ".join(sorted(self.game.items)) if self.game.items else "vide")
                + "  |  Étapes parcourues : " + str(len(self.game.history)))
            while self.choices_layout.count():
                item = self.choices_layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
            if self.game.finished:
                self.status.setText("FIN : " + node["ending"] + " | Nouvelle partie pour réessayer.")
            else:
                for index, option in enumerate(self.game.choices()):
                    button = QPushButton(option["label"])
                    button.setMinimumHeight(34)
                    button.clicked.connect(lambda ignored=False, i=index: self.choose(i))
                    self.choices_layout.addWidget(button)
                self.status.setText("Choisir une option pour poursuivre. La progression est sauvegardée automatiquement.")

        def choose(self, index):
            try:
                self.game.choose(index)
                self.game.save(args.save)
                self.render()
            except (StoryError, OSError, TypeError) as error:
                QMessageBox.warning(self, "Action impossible", str(error))
                self.render()

        def save(self):
            try:
                self.game.save(args.save)
                self.status.setText("Partie sauvegardée.")
            except (OSError, TypeError) as error:
                QMessageBox.warning(self, "Sauvegarde impossible", str(error))

        def load(self):
            try:
                self.game = GameSession.restore(self.story, args.save)
                self.render()
            except (OSError, ValueError, TypeError) as error:
                QMessageBox.warning(self, "Chargement impossible", str(error))
                self.render()

        def restart(self):
            self.game = GameSession(self.story)
            self.save()
            self.render()

    app = QApplication([])
    window = AdventureWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    raise SystemExit(main())
