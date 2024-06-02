from PySide6.QtCore import (QCoreApplication, QRect, Qt)
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QMainWindow, QFrame, QGridLayout, QLabel, QPushButton, QSizePolicy, QWidget, QVBoxLayout,
                               QSpacerItem)


class RetourCamera(QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.label = QLabel(self)
		self.label.setObjectName("label")
		self.label.setFrameShape(QFrame.Box)
		self.label.setLineWidth(3)
		self.label.setPixmap(QPixmap("C:\\Users\\quent\\Downloads\\robot.webp"))
		self.label.setScaledContents(True)

		layout = QVBoxLayout()
		layout.addWidget(self.label)
		self.setLayout(layout)


class FlechesDirectionnels(QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.gridLayout = QGridLayout(self)
		self.buttons = []
		directions = [ "↖️", "⬆️", "↗️", "⬅️","🔨",  "➡️","","⬇️","" ]
		for i, direction in enumerate(directions):
			button = QPushButton(direction, self)
			if(direction == ""):
				button.setDisabled(True)
			button.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
			self.buttons.append(button)
			self.gridLayout.addWidget(button, i // 3, i % 3)


class BoutonsActions(QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.gridLayout = QGridLayout(self)
		self.buttons = []
		actions = ["🕺\nDanse", "🍑\nWiggle", "🎉\nCélébrer", "🧍\nDebout", "👀\nYeux", "⚽\nTir", "💃\nDance circulaire",
		           "PushButton"]
		for action in actions:
			button = QPushButton(action, self)
			button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
			self.buttons.append(button)
			self.gridLayout.addWidget(button, len(self.buttons) // 4, len(self.buttons) % 4)


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.centralwidget = QWidget(self)
		self.setCentralWidget(self.centralwidget)
		self.centralLayout = QVBoxLayout(self.centralwidget)

		# Setup camera return widget
		self.retour_camera = RetourCamera(self.centralwidget)
		self.retour_camera.setFixedSize(500, 350)  # Adjust size as needed
		self.centralLayout.addWidget(self.retour_camera)

		# Spacer
		self.centralLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

		# Setup directional buttons
		self.fleches_directionnelles = FlechesDirectionnels(self.centralwidget)
		self.fleches_directionnelles.setFixedHeight(150)  # Adjust size as needed
		self.centralLayout.addWidget(self.fleches_directionnelles)

		# Spacer
		self.centralLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

		# Setup action buttons
		self.boutons_actions = BoutonsActions(self.centralwidget)
		self.boutons_actions.setFixedHeight(100)  # Adjust size as needed
		self.centralLayout.addWidget(self.boutons_actions)

		# Spacer
		self.centralLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

		# Setup label block
		self.label_block = QLabel("Label Block", self.centralwidget)
		self.label_block.setAlignment(Qt.AlignCenter)
		self.label_block.setFixedHeight(50)  # Adjust size as needed
		self.centralLayout.addWidget(self.label_block)

		self.setWindowTitle("MainWindow")


if __name__ == "__main__":
	import sys
	from PySide6.QtWidgets import QApplication

	app = QApplication(sys.argv)
	mainWin = MainWindow()
	mainWin.show()
	sys.exit(app.exec())
