from martypy import Marty
from marty_perso import MartyPerso


marty1 = MartyPerso()
marty1.setIP("127.0.0.1")
marty2 = MartyPerso()
marty2.setIP("127.0.0.1")

Couleurs = {
    "red": "Fin",
    "lightblue": "Depart",
    "green": "Est",
    "yellow": "Ouest",
    "darkblue": "Sud",
    "pink": "Nord",
    "black": "Vide"
}


def LireCouleur(marty):
    return marty.get_sensor_color()

def Avancer(robot, direction):
    if direction == "Nord":
        robot.walk(2, direction='forward')
    elif direction == "Sud":
        robot.walk(2, direction='backward')
    elif direction == "Est":
        robot.walk(3, direction='right')
    elif direction == "Ouest":
        robot.walk(4, direction='left')

couleur_actuelle = LireCouleur(marty2)
direction = Couleurs[couleur_actuelle]
while direction != "Fin":
    Avancer(marty1, direction)
    marty1.stop()
    couleur_actuelle = LireCouleur(marty1)
    direction = Couleurs[couleur_actuelle]

couleur_actuelle = LireCouleur(marty2)
direction = Couleurs[couleur_actuelle]
while direction != "Fin":
    Avancer(marty2, direction)
    marty2.stop()
    couleur_actuelle = LireCouleur(marty2)
    direction = Couleurs[couleur_actuelle]


if LireCouleur(marty1) == "red" and LireCouleur(marty2) == "red":
    marty1.celebrate()
    marty2.celebrate()
