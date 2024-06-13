from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QGridLayout, QPushButton
from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QColor, QIcon
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QWidget


def set_svg_icon(self, button, svg_path, size: tuple[int, int] = (64, 64)):
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

        self.eyes_button = QPushButton("\nYeux", self)
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

