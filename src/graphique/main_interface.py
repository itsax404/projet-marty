from PySide6.QtCore import Qt, QTimer, QSize
from PySide6.QtGui import QColor, QIcon, QPixmap, QFont, QPainter
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QMainWindow, QGridLayout, QLabel, QPushButton, QWidget, QSizePolicy, QHBoxLayout, \
    QMessageBox, QLineEdit, QVBoxLayout, QFrame
from ..python.marty_perso import MartyPerso

expanding_police = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding);


def set_svg_icon(self, button, svg_path, size: tuple[int, int] = (128, 128)):
    renderer = QSvgRenderer(svg_path)
    icon_size = QSize(size[0], size[1])
    pixmap = QPixmap(icon_size)
    pixmap.fill(QColor("transparent"))

    painter = QPainter(pixmap)
    renderer.render(painter)
    painter.end()

    icon = QIcon(pixmap)
    button.setIcon(icon)
    button.setIconSize(icon_size)
    return button


class InfoWidget(QWidget):
    def __init__(self, parent=None, marty=None):
        super().__init__(parent)

        self.marty = marty

        self.initUI()
        self.start_timer()

    def initUI(self):
        main_layout = QVBoxLayout()

        frame = QFrame(self)
        frame.setFrameShape(QFrame.Box)
        frame.setLineWidth(2)

        grid = QGridLayout()
        frame.setLayout(grid)

        header_battery = QLabel("Batterie")
        header_distance = QLabel("Distance")
        header_color = QLabel("Capteur de couleur")
        header_connected = QLabel("Connecté")

        font = QFont()
        font.setBold(True)
        header_battery.setFont(font)
        header_distance.setFont(font)
        header_color.setFont(font)
        header_connected.setFont(font)

        header_battery.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_distance.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_color.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_connected.setAlignment(Qt.AlignmentFlag.AlignCenter)

        grid.addWidget(header_battery, 0, 0)
        grid.addWidget(header_distance, 0, 1)
        grid.addWidget(header_color, 0, 2)
        grid.addWidget(header_connected, 0, 3)

        self.battery_label = QLabel()
        self.distance_label = QLabel()
        self.color_label = QLabel()
        self.connected_label = QLabel()

        self.battery_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.distance_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.color_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.connected_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        grid.addWidget(self.battery_label, 1, 0)
        grid.addWidget(self.distance_label, 1, 1)
        grid.addWidget(self.color_label, 1, 2)
        grid.addWidget(self.connected_label, 1, 3)

        main_layout.addWidget(frame)
        self.setLayout(main_layout)

        self.setGeometry(300, 300, 400, 200)

        self.update_values()

    def start_timer(self):
        # Create a QTimer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_values)
        self.timer.start(1000)  # Timeout interval is 1000 ms or 1 second

    def update_values(self):
        # Update the values in the labels
        self.battery_label.setText(self.marty.get_battery_level())
        self.distance_label.setText(self.marty.get_distance())
        self.color_label.setText(self.marty.get_color_sensor())
        self.connected_label.setText("🟢" if self.marty.is_connected() else "🔴")


class IPBlock(QWidget):

    def __init__(self, parent=None, marty=None):
        super().__init__(parent)

        self.marty = marty

        self.ip_entry = QLineEdit(self)
        self.ip_entry.setPlaceholderText("Entrez l'adresse IP")

        self.connect_button = QPushButton("Connecter", self)
        self.connect_button.clicked.connect(self.on_button_click)

        layout = QHBoxLayout()
        layout.addWidget(self.ip_entry, 2)
        layout.addWidget(self.connect_button)

        self.setLayout(layout)

        self.setWindowTitle("Connexion IP")
        self.setGeometry(300, 300, 300, 200)

    def on_button_click(self):
        if self.connect_button.text() == "Connecter":
            ip_address = self.ip_entry.text()
            if ip_address:
                QMessageBox.information(self, "Adresse IP", f"Connecté à l'adresse IP : {ip_address}")
                self.marty.setIP(ip_address)
                self.ip_entry.setDisabled(True)
                self.connect_button.setText("Déconnecter")
            else:
                QMessageBox.warning(self, "Erreur", "Veuillez entrer une adresse IP valide.")
        else:
            self.ip_entry.setDisabled(False)
            self.marty.disconnect()
            self.connect_button.setText("Connecter")


class DirectionalsArrows(QWidget):
    def __init__(self, parent=None, marty=None):
        super().__init__(parent)
        self.marty = marty

        self.gridLayout = QGridLayout(self)

        self.left_button = QPushButton("", self)
        self.left_button = set_svg_icon(self, self.left_button, "src/graphique/icons/arrows/left_arrow.svg")
        self.left_button.clicked.connect(self.marty.move_left)
        # self.left_button.setSizePolicy(expanding_police)
        self.gridLayout.addWidget(self.left_button, 2, 0, 1, 1)

        self.turn_left_button = QPushButton("", self)
        self.turn_left_button = set_svg_icon(self, self.turn_left_button, "src/graphique/icons/arrows/turn_left.svg")
        self.turn_left_button.clicked.connect(self.marty.turn_left)
        # self.turn_left_button.setSizePolicy(expanding_police)
        self.gridLayout.addWidget(self.turn_left_button, 1, 0, 1, 1)

        self.up_button = QPushButton("", self)
        self.up_button = set_svg_icon(self, self.up_button, "src/graphique/icons/arrows/up_arrow.svg")
        self.up_button.clicked.connect(self.marty.move_forward)
        # self.up_button.setSizePolicy(expanding_police)
        self.gridLayout.addWidget(self.up_button, 1, 1, 1, 1)

        self.central_button = QPushButton("", self)
        self.central_button = set_svg_icon(self, self.central_button, "src/graphique/icons/arrows/central_element.svg")
        self.central_button.setDisabled(True)
        # self.central_button.setSizePolicy(expanding_police)
        self.gridLayout.addWidget(self.central_button, 2, 1, 1, 1)

        self.down_button = QPushButton("", self)
        self.down_button = set_svg_icon(self, self.down_button, "src/graphique/icons/arrows/down_arrow.svg")
        self.down_button.clicked.connect(self.marty.move_backward)
        # self.down_button.setSizePolicy(expanding_police)
        self.gridLayout.addWidget(self.down_button, 3, 1, 1, 1)

        self.right_button = QPushButton("", self)
        self.right_button = set_svg_icon(self, self.right_button, "src/graphique/icons/arrows/right_arrow.svg")
        self.right_button.clicked.connect(self.marty.move_right)
        # self.right_button.setSizePolicy(expanding_police)
        self.gridLayout.addWidget(self.right_button, 2, 2, 1, 1)

        self.turn_right_button = QPushButton("", self)
        self.turn_right_button = set_svg_icon(self, self.turn_right_button, "src/graphique/icons/arrows/turn_right.svg")
        self.turn_right_button.clicked.connect(self.marty.turn_right)

        # self.turn_right_button.setSizePolicy(expanding_police)
        self.gridLayout.addWidget(self.turn_right_button, 1, 2, 1, 1)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Left:
            self.marty.move_left()
        elif event.key() == Qt.Key.Key_Right:
            self.marty.move_right()
        elif event.key() == Qt.Key.Key_Up:
            self.marty.move_forward()
        elif event.key() == Qt.Key.Key_Down:
            self.marty.move_backward()


class ActionsBlocks(QWidget):
    def __init__(self, parent=None, marty=None):
        super().__init__(parent)

        self.marty = marty

        self.gridLayout = QGridLayout(self)

        self.dance_button = QPushButton("🕺\nDanse", self)
        self.dance_button.clicked.connect(self.marty.dance)
        # self.dance_button.setSizePolicy(expanding_police)
        self.gridLayout.addWidget(self.dance_button, 0, 0, 1, 1)

        self.circular_dance = QPushButton("💃\nDance circulaire", self)
        self.circular_dance.clicked.connect(self.marty.circular_dance)
        # self.circular_dance.setSizePolicy(expanding_police)
        self.gridLayout.addWidget(self.circular_dance, 1, 2, 1, 1)

        self.kick_button = QPushButton("⚽\nTir", self)
        self.kick_button.clicked.connect(self.marty.kick)
        # self.kick_button.setSizePolicy(expanding_police)
        self.gridLayout.addWidget(self.kick_button, 1, 1, 1, 1)

        self.eyes_button = QPushButton("", self)
        self.eyes_button = set_svg_icon(self, self.eyes_button, "src/graphique/icons/actions/eyes.svg")
        self.eyes_button.clicked.connect(self.marty.eyes)
        # self.eyes_button.setSizePolicy(expanding_police)
        self.gridLayout.addWidget(self.eyes_button, 1, 0, 1, 1)

        self.celebrate_button = QPushButton("🎉\nCélébrer", self)
        self.celebrate_button.clicked.connect(self.marty.celebrate)
        # self.celebrate_button.setSizePolicy(expanding_police)
        self.gridLayout.addWidget(self.celebrate_button, 0, 2, 1, 1)

        self.wiggle_eyes_buttons = QPushButton("🍑\nWiggle", self)
        self.wiggle_eyes_buttons.clicked.connect(self.marty.wiggle_eyes)
        # self.wiggle_eyes_buttons.setSizePolicy(expanding_police)
        self.gridLayout.addWidget(self.wiggle_eyes_buttons, 0, 1, 1, 1)

        self.rab = QPushButton("Stop", self)
        self.rab.clicked.connect(self.marty.stop)
        # self.rab.setSizePolicy(expanding_police)
        self.gridLayout.addWidget(self.rab, 1, 3, 1, 1)

        self.stand_button = QPushButton("🧍\nDebout", self)
        self.stand_button.clicked.connect(self.marty.stand_up)
        # self.stand_button.setSizePolicy(expanding_police)
        self.gridLayout.addWidget(self.stand_button, 0, 3, 1, 1)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.marty = MartyPerso()
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


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
