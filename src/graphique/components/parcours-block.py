from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton


class ParcoursBlock(QWidget):
    def __init__(self, parent=None, martys_controller=None, marty_name=""):
        super().__init__(parent)

        self.martys_controller = martys_controller
        self.marty_name = marty_name

        self.gridLayout = QHBoxLayout(self)

        self.buttonScan = QPushButton("Lancer le scan du parcours", self)
        if(marty_name == "marty1"):
            self.buttonScan.clicked.connect(self.martys_controller.explorer_marty_1)
        elif(marty_name == "marty2"):
            self.buttonScan.clicked.connect(self.martys_controller.explorer_marty_2)

        self.buttonParcours = QPushButton("Lancer le parcours final", self)
        # if (marty_name == "marty1"):
        #     self.buttonParcours.clicked.connect(self.martys_controller.explorer_marty_1)
        # elif (marty_name == "marty2"):
        #     self.buttonParcours.clicked.connect(self.martys_controller.explorer_marty_2)
        self.gridLayout.addWidget(self.buttonScan, Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.buttonParcours, Qt.AlignmentFlag.AlignCenter)
