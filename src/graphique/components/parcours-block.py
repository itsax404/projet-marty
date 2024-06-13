from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton


class ParcoursBlock(QWidget):
    def __init__(self, parent=None, marty=None):
        super().__init__(parent)

        self.marty = marty

        self.gridLayout = QHBoxLayout(self)

        self.buttonScan = QPushButton("Lancer le scan du parcours", self)
        self.buttonScan.clicked.connect(self.marty.explorer)

        self.buttonParcours = QPushButton("Lancer le parcours final", self)
        # self.buttonParcours.clicked.connect()

        self.gridLayout.addWidget(self.buttonScan, Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.buttonParcours, Qt.AlignmentFlag.AlignCenter)
