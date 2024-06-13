from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QVBoxLayout, QFrame, QGridLayout, QLabel

from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QColor, QPainter, QIcon
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

expanding_police = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

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
        header_color = QLabel("Capteur de couleur")
        header_connected = QLabel("Connecté")
        header_name = QLabel("Nom de Marty")

        font = QFont()
        font.setBold(True)
        header_battery.setFont(font)
        header_color.setFont(font)
        header_connected.setFont(font)
        header_name.setFont(font)

        header_battery.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_color.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_connected.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        grid.addWidget(header_battery, 0, 0)
        grid.addWidget(header_color, 0, 1)
        grid.addWidget(header_connected, 0, 2)
        grid.addWidget(header_name, 0, 3)

        self.battery_label = QLabel()
        self.color_label = QLabel()
        self.connected_label = QLabel()
        self.marty_name_label = QLabel()

        self.battery_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.color_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.connected_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.marty_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        grid.addWidget(self.battery_label, 1, 0)
        grid.addWidget(self.color_label, 1, 1)
        grid.addWidget(self.connected_label, 1, 2)
        grid.addWidget(self.marty_name_label, 1, 3)

        main_layout.addWidget(frame)
        self.setLayout(main_layout)

        self.setGeometry(300, 300, 400, 200)

        self.update_values()

    def start_timer(self):
        # Create a QTimer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_values)
        self.timer.start(500)

    def update_values(self):
        if(self.marty.is_connected()):
            self.battery_label.setText(f"{self.marty.get_battery_level()} %")
            self.color_label.setText(self.marty.get_color_sensor())
        self.connected_label.setText("🟢" if self.marty.is_connected() else "🔴")
        self.marty_name_label.setText(self.marty.get_name() if self.marty.is_connected() else "Pas connecté")
