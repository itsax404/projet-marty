import random
from PySide6.QtCore import QCoreApplication, Qt
from PySide6.QtGui import QColor, QIcon, QPixmap
from PySide6.QtWidgets import QMainWindow, QGridLayout, QLabel, QPushButton, QWidget, QSizePolicy

expanding_police = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding);


class DirectionalsArrows(QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)


		self.gridLayout = QGridLayout(self)

		self.left_button = QPushButton("⬅️", self)
		self.left_button.setSizePolicy(expanding_police)
		self.gridLayout.addWidget(self.left_button, 2, 0, 1, 1)

		self.turn_left_button = QPushButton("↖️", self)
		self.turn_left_button.setSizePolicy(expanding_police)
		self.gridLayout.addWidget(self.turn_left_button, 1, 0, 1, 1)

		self.up_button = QPushButton("⬆️", self)
		self.up_button.setSizePolicy(expanding_police)
		self.gridLayout.addWidget(self.up_button, 1, 1, 1, 1)

		self.central_button = QPushButton("🔶", self)
		self.central_button.setDisabled(True)
		self.central_button.setSizePolicy(expanding_police)
		self.gridLayout.addWidget(self.central_button, 2, 1, 1, 1)

		self.down_button = QPushButton("⬇️", self)
		self.down_button.setSizePolicy(expanding_police)
		self.gridLayout.addWidget(self.down_button, 3, 1, 1, 1)

		self.right_button = QPushButton("➡️", self)
		self.right_button.setSizePolicy(expanding_police)
		self.gridLayout.addWidget(self.right_button, 2, 2, 1, 1)

		self.turn_right_button = QPushButton("↗️", self)
		self.turn_right_button.setSizePolicy(expanding_police)
		self.gridLayout.addWidget(self.turn_right_button, 1, 2, 1, 1)


class ActionsBlocks(QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.gridLayout = QGridLayout(self)

		self.dance_button = QPushButton("🕺\nDanse", self)
		self.dance_button.setSizePolicy(expanding_police)
		self.gridLayout.addWidget(self.dance_button, 0, 0, 1, 1)

		self.circular_dance = QPushButton("💃\nDance circulaire", self)
		self.circular_dance.setSizePolicy(expanding_police)
		self.gridLayout.addWidget(self.circular_dance, 1, 2, 1, 1)

		self.kick_button = QPushButton("⚽\nTir", self)
		self.kick_button.setSizePolicy(expanding_police)
		self.gridLayout.addWidget(self.kick_button, 1, 1, 1, 1)

		self.eyes_button = QPushButton("👀\nYeux", self)
		self.eyes_button.setSizePolicy(expanding_police)
		self.gridLayout.addWidget(self.eyes_button, 1, 0, 1, 1)

		self.celebrate_button = QPushButton("🎉\nCélébrer", self)
		self.celebrate_button.setSizePolicy(expanding_police)
		self.gridLayout.addWidget(self.celebrate_button, 0, 2, 1, 1)

		self.wiggle_eyes_buttons = QPushButton("🍑\nWiggle", self)
		self.wiggle_eyes_buttons.setSizePolicy(expanding_police)
		self.gridLayout.addWidget(self.wiggle_eyes_buttons, 0, 1, 1, 1)

		self.rab = QPushButton("temp", self)
		self.rab.setSizePolicy(expanding_police)
		self.gridLayout.addWidget(self.rab, 1, 3, 1, 1)

		self.stand_button = QPushButton("🧍\nDebout", self)
		self.stand_button.setSizePolicy(expanding_police)
		self.gridLayout.addWidget(self.stand_button, 0, 3, 1, 1)


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setObjectName("Contrôle de Marty")
		self.resize(800, 601)
		self.centralwidget = QWidget(self)
		self.setCentralWidget(self.centralwidget)
		self.layout = QGridLayout(self.centralwidget)

		self.directional_arrows = DirectionalsArrows(self.centralwidget)
		self.actions_block = ActionsBlocks(self.centralwidget)

		self.layout.addWidget(self.directional_arrows, 0, 3)
		self.layout.addWidget(self.actions_block, 0, 1)

		self.layout.setColumnStretch(0, 1)
		self.layout.setColumnStretch(1, 1)
		self.layout.setColumnStretch(2, 1)
		self.layout.setColumnStretch(3, 1)


if __name__ == "__main__":
	import sys
	from PySide6.QtWidgets import QApplication

	app = QApplication(sys.argv)
	mainWin = MainWindow()
	mainWin.show()
	sys.exit(app.exec())
