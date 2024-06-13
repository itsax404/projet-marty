from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QColor, QPainter, QIcon
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

expanding_police = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)


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


