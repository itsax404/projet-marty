from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QHBoxLayout, QMessageBox


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
