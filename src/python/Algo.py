from martypy import Marty
from color import creer_image_couleur

marty1 = Marty("192.168.0.100")
marty2 = Marty("192.168.0.101")


Couleurs = {
    "Rouge": "Nord",
    "Bleu": "Sud",
    "Vert": "Est",
    "Jaune": "Ouest",
    "Violet": "Arrêt"
}


def LireCouleur(marty):
    return creer_image_couleur(marty.get_color_sensor_hex("LeftColorSensor"))

def Avancer(robot, direction):
    if direction == "Nord":
        robot.walk(2, direction='forward')
    elif direction == "Sud":
        robot.walk(2, direction='backward')
    elif direction == "Est":
        robot.walk(3, direction='right')
    elif direction == "Ouest":
        robot.walk(4, direction='left')

while True:
    couleur_actuelle = LireCouleur(marty1)
    direction = Couleurs.get(couleur_actuelle, "Arrêt")
    if direction == "Arrêt":
        break
    Avancer(marty1, direction)
    marty1.stop()


while True:
    couleur_actuelle = LireCouleur(marty2)
    direction = Couleurs.get(couleur_actuelle, "Arrêt")
    if direction == "Arrêt":
        break
    Avancer(marty2, direction)
    marty2.stop()


if LireCouleur(marty1) == "Violet" and LireCouleur(marty2) == "Violet":
    marty1.celebrate()
    marty2.celebrate()
