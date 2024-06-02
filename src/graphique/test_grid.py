from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QMainWindow, QSpacerItem, QSizePolicy, QLabel, QGridLayout, QPushButton

import random
police = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

class TestWidget(QWidget):

	def __random_color__(self):
		hexaValue = hex(random.getrandbits(24))
		return str(hexaValue).split("x")[1]
	def __init__(self):
		super().__init__()
		value = self.__random_color__()
		print(value)
		self.bouton = QPushButton(value, self)
		self.bouton.setSizePolicy(police)

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.centralwidget = QWidget(self)
		self.setCentralWidget(self.centralwidget)
		self.centralLayout = QGridLayout(self.centralwidget)

		self.testWidget1 = TestWidget()
		self.centralLayout.addWidget(self.testWidget1, 0, 0)

		self.testWidget2 = TestWidget()
		self.centralLayout.addWidget(self.testWidget2, 0, 1)

		self.testWidget3 = TestWidget()
		self.centralLayout.addWidget(self.testWidget3, 1, 0, 1, 2)

		self.centralLayout.setColumnStretch(0, 1)
		self.centralLayout.setColumnStretch(1, 1)
		self.centralLayout.setRowStretch(0, 1)
		self.centralLayout.setRowStretch(1,1)

		self.setWindowTitle("MainWindow")


if __name__ == "__main__":
	import sys
	from PySide6.QtWidgets import QApplication, QWidget, QMainWindow

	app = QApplication(sys.argv)
	mainWin = MainWindow()
	mainWin.show()
	sys.exit(app.exec())
