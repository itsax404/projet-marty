from martypy import Marty
from marty_perso import MartyPerso
from collections import deque



"""
marty1 = MartyPerso()
marty1.setIP("127.0.0.1")
marty2 = MartyPerso()
marty2.setIP("127.0.0.1")
"""

Couleurs = {
    "red": "Fin",
    "lightblue": "Depart",
    "green": "Nord",
    "yellow": "Sud",
    "darkblue": "Est",
    "pink": "Ouest",
    "black": "black"
}

parcours1 = [
    ["black", "black", "black"],
    ["green", "green", "yellow"],
    ["lightblue", "green", "red"]
]

parcours2 = [
    ["green", "darkblue", "yellow"],
    ["black", "black", "black"],
    ["lightblue", "black", "red"]
]


def fusion(tab1, tab2):
    tab3 = [
        ["black", "black", "black"],
        ["black", "black", "black"],
        ["black", "black", "black"]
    ]
    for i in range(3):
        for j in range(3):
            if(tab1[i][j] == "black"):
                tab3[i][j] = tab2[i][j]
            if(tab2[i][j] == "black"):
                tab3[i][j] = tab1[i][j]
            if(tab1[i][j] == "lightblue" or tab1[i][j] == "red"):
                tab3[i][j] = tab1[i][j]
    return tab3

parcours3 = fusion(parcours1, parcours2)
print(parcours3)
def getVoisins(parcours):
    voisins = [
        [
            {'haut': 'black', 'bas' : 'black', 'gauche' : 'black', 'droite' : 'black'},
            {'haut': 'black', 'bas' : 'black', 'gauche' : 'black', 'droite' : 'black'},
            {'haut': 'black', 'bas' : 'black', 'gauche' : 'black', 'droite' : 'black'}
        ],
        [
            {'haut': 'black', 'bas' : 'black', 'gauche' : 'black', 'droite' : 'black'},
            {'haut': 'black', 'bas' : 'black', 'gauche' : 'black', 'droite' : 'black'},
            {'haut': 'black', 'bas' : 'black', 'gauche' : 'black', 'droite' : 'black'}
        ],
        [
            {'haut': 'black', 'bas' : 'black', 'gauche' : 'black', 'droite' : 'black'},
            {'haut': 'black', 'bas' : 'black', 'gauche' : 'black', 'droite' : 'black'},
            {'haut': 'black', 'bas' : 'black', 'gauche' : 'black', 'droite' : 'black'}
        ]
    ]
    
    for i in range(3):
        for j in range(3):
            for key in voisins[i][j]:
                if(key == 'haut'):
                    if(i-1 >= 0):
                        voisins[i][j][key] = parcours[i-1][j]
                elif(key == 'bas'):
                    if(i+1 < 3):
                        voisins[i][j][key] = parcours[i+1][j]
                elif(key == 'droite'):
                    if(j+1 < 3):
                        voisins[i][j][key] = parcours[i][j+1]
                else:
                    if(j-1 >= 0):
                        voisins[i][j][key] = parcours[i][j-1]
    return voisins

voisins = getVoisins(parcours3)

def getDebutFin(parcours):
    xDepart, yDepart, xFin, yFin = 0, 0, 0, 0
    for i in range(3):
        for j in range(3):
            if(parcours[i][j] == "lightblue"):
                xDepart = i
                yDepart = j
            if(parcours[i][j] == "red"):
                xFin = i
                yFin = j
    return ((xDepart, yDepart),(xFin, yFin))
    
debut, fin = getDebutFin(parcours3)

def getChemins(debut, fin, voisins, parcours):
    lst = voisins[debut[0]][debut[1]]
    chemin = []
    for voisin, value in lst.items():
        if(value != "black" and value != "red"):
            essai = [value]
            print(voisin)
            x, y = debut
            if(voisin == "haut"):
                x -= 1
            elif(voisin == "bas"):
                x += 1
            elif(voisin == "droite"):
                y += 1
            else:
                y -= 1
            continuer = True
            while((x, y) != fin and continuer == True):
                if(parcours[x][y] == "green" and x > 0):
                    x -= 1
                elif(parcours[x][y] == "yellow" and x < 2):
                    x += 1
                elif(parcours[x][y] == "darkblue" and y < 2):
                    y += 1
                elif(parcours[x][y] == "pink" and y > 0):
                    y -= 1
                else:
                    continuer = False
                print(x, y)
                essai.append(parcours[x][y])
            if(essai[-1] == "red"):
                chemin = essai
    return chemin

chemin = getChemins(debut, fin, voisins, parcours3)
print(chemin)


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

"""
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
"""