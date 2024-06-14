from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QMainWindow, QGridLayout
from ultraimport import ultraimport

IPBlock = ultraimport("__dir__/components/ip-block.py", "IPBlock")
InfoWidget = ultraimport("__dir__/components/infos-marty.py", "InfoWidget")
ParcoursBlock = ultraimport("__dir__/components/parcours-block.py", "ParcoursBlock")
MartyPerso = ultraimport("__dir__/../python/marty_perso.py", "MartyPerso")
MartysController = ultraimport("__dir__/../python/martys_controller.py", "MartysController")


class ParcoursInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.marty1 = MartyPerso("Marty1")
        self.marty2 = MartyPerso("Marty2")

        self.martys_controller = MartysController(self.marty1, self.marty2)

        self.setObjectName("Contrôle des Marty")
        self.resize(800, 601)
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.layout = QGridLayout(self.centralwidget)

        self.ip_block1 = IPBlock(self.centralwidget, self.marty1)
        self.ip_block2 = IPBlock(self.centralwidget, self.marty2)

        self.infos_block1 = InfoWidget(self.centralwidget, self.marty1)
        self.infos_block2 = InfoWidget(self.centralwidget, self.marty2)

        self.parcours_block1 = ParcoursBlock(self.centralwidget, self.martys_controller, "marty1")

        self.layout.addWidget(self.ip_block1, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.infos_block1, 0, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.ip_block2, 1, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.infos_block2, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.parcours_block1, 0, 2, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.parcours_block2, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    mainWin = ParcoursInterface()
    mainWin.show()
    sys.exit(app.exec())
