import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit

# define the start of the game
def start_game():
    global choice
    choice = None
    instructions.setText("Welcome to the game! You are a brave adventurer exploring a mysterious cave. You come to a fork in the path and see two tunnels. One tunnel is dark and narrow, the other is well-lit but looks longer. Do you go left or right?")
    left_button.show()
    right_button.show()

# handle the player's choice
def handle_choice(direction):
    global choice
    choice = direction
    if choice == "left":
        instructions.setText("You choose the dark, narrow tunnel. You walk for what seems like hours, until you finally see a faint light up ahead. As you get closer, you realize it's a small opening to the outside. You crawl through the opening and find yourself back at the entrance of the cave. You made it out! Congratulations!")
    elif choice == "right":
        instructions.setText("You choose the well-lit, longer tunnel. You walk for a while, until you come to a room filled with treasure. You start to fill your pockets with gold and jewels, when you hear a loud rumbling noise. Suddenly, the room starts to shake and you realize the treasure was protected by a trap! You barely make it out alive, but you managed to grab some treasure on your way out. Not a bad haul, all things considered.")
    left_button.hide()
    right_button.hide()

# create the application and the main window
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Text-Based Role-Playing Game")
window.setFixedSize(400, 300)  # set the size of the window

# create the instructions text edit and the buttons
instructions = QTextEdit()
instructions.setText("Press 'Start Game' to begin.")
left_button = QPushButton("Left")
left_button.clicked.connect(lambda: handle_choice("left"))
right_button = QPushButton("Right")
right_button.clicked.connect(lambda: handle_choice("right"))
start_button = QPushButton("Start Game")
start_button.clicked.connect(start_game)

# create the layout and add the widgets
layout = QVBoxLayout()
layout.addWidget(instructions)
layout.addWidget(left_button)
layout.addWidget(right_button)
layout.addWidget(start_button)
window.setLayout(layout)

# show the window and run the application
window.show()
sys.exit(app.exec_())
