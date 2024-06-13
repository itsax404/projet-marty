from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QGridLayout, QWidget
from ultraimport import ultraimport

DirectionalsArrows = ultraimport("__dir__/../graphique/components/directionnal-arrows.py", "DirectionalsArrows")
ActionsBlocks = ultraimport("__dir__/../graphique/components/actions-block.py", "ActionsBlocks")
IPBlock = ultraimport("__dir__/../graphique/components/ip-block.py", "IPBlock")
InfoWidget = ultraimport("__dir__/../graphique/components/infos-marty.py", "InfoWidget")

MartyPerso = ultraimport("__dir__/../python/marty_perso.py", "MartyPerso")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.marty = MartyPerso("marty1")
        self.setObjectName("Contrôle de Marty")
        self.resize(800, 601)
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.layout = QGridLayout(self.centralwidget)

        self.directional_arrows = DirectionalsArrows(self.centralwidget, self.marty)
        self.actions_block = ActionsBlocks(self.centralwidget, self.marty)
        self.ip_block = IPBlock(self.centralwidget, self.marty)
        self.infos_block = InfoWidget(self.centralwidget, self.marty)

        self.layout.addWidget(self.ip_block, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.infos_block, 0, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.directional_arrows, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.actions_block, 1, 0, alignment=Qt.AlignmentFlag.AlignCenter)

    def keyPressEvent(self, event):
        print("as")
        if event.key() == Qt.Key.Key_Q:
            self.marty.move_left()
        elif event.key() == Qt.Key.Key_D:
            self.marty.move_right()
        elif event.key() == Qt.Key.Key_Z:
            self.marty.move_forward()
        elif event.key() == Qt.Key.Key_S:
            self.marty.move_backward()
        elif event.key() == Qt.Key.Key_A:
            self.marty.turn_left()
        elif event.key() == Qt.Key.Key_E:
            self.marty.turn_right()

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
