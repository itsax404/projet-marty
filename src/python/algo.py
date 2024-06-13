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


class Algo:
    def __init__(self, grille1=None, grille2=None):
        self.parcours1 = grille1
        self.parcours2 = grille2

    def fusion(self, tab1, tab2):

        tab3 = [
            ["black", "black", "black"],
            ["black", "black", "black"],
            ["black", "black", "black"]
        ]
        for i in range(3):
            for j in range(3):
                if (tab1[i][j] == "black"):
                    tab3[i][j] = tab2[i][j]
                if (tab2[i][j] == "black"):
                    tab3[i][j] = tab1[i][j]
                if (tab1[i][j] == "lightblue" or tab1[i][j] == "red"):
                    tab3[i][j] = tab1[i][j]
        return tab3

    def getVoisins(self, parcours):
        voisins = [
            [
                {'haut': 'black', 'bas': 'black', 'gauche': 'black', 'droite': 'black'},
                {'haut': 'black', 'bas': 'black', 'gauche': 'black', 'droite': 'black'},
                {'haut': 'black', 'bas': 'black', 'gauche': 'black', 'droite': 'black'}
            ],
            [
                {'haut': 'black', 'bas': 'black', 'gauche': 'black', 'droite': 'black'},
                {'haut': 'black', 'bas': 'black', 'gauche': 'black', 'droite': 'black'},
                {'haut': 'black', 'bas': 'black', 'gauche': 'black', 'droite': 'black'}
            ],
            [
                {'haut': 'black', 'bas': 'black', 'gauche': 'black', 'droite': 'black'},
                {'haut': 'black', 'bas': 'black', 'gauche': 'black', 'droite': 'black'},
                {'haut': 'black', 'bas': 'black', 'gauche': 'black', 'droite': 'black'}
            ]
        ]

        for i in range(3):
            for j in range(3):
                for key in voisins[i][j]:
                    if (key == 'haut'):
                        if (i - 1 >= 0):
                            voisins[i][j][key] = parcours[i - 1][j]
                    elif (key == 'bas'):
                        if (i + 1 < 3):
                            voisins[i][j][key] = parcours[i + 1][j]
                    elif (key == 'droite'):
                        if (j + 1 < 3):
                            voisins[i][j][key] = parcours[i][j + 1]
                    else:
                        if (j - 1 >= 0):
                            voisins[i][j][key] = parcours[i][j - 1]
        return voisins

    def getDebutFin(self, parcours):
        xDepart, yDepart, xFin, yFin = 0, 0, 0, 0
        for i in range(3):
            for j in range(3):
                if (parcours[i][j] == "lightblue"):
                    xDepart = i
                    yDepart = j
                if (parcours[i][j] == "red"):
                    xFin = i
                    yFin = j
        return ((xDepart, yDepart), (xFin, yFin))

    def getChemins(self):
        parcoursFusionne = self.fusion(self.parcours1, self.parcours2)
        debut, fin = self.getDebutFin(parcoursFusionne)
        voisins = self.getVoisins(parcoursFusionne)
        lst = voisins[debut[0]][debut[1]]
        chemin = []
        for voisin, value in lst.items():
            if (value != "black" and value != "red"):
                essai = []
                print(voisin)
                x, y = debut
                if (voisin == "haut"):
                    essai.append("green")
                    x -= 1
                elif (voisin == "bas"):
                    essai.append("yellow")
                    x += 1
                elif (voisin == "droite"):
                    essai.append("darkblue")
                    y += 1
                else:
                    essai.append("pink")
                    y -= 1
                essai.append(voisin)
                continuer = True
                while ((x, y) != fin and continuer == True):
                    if (parcoursFusionne[x][y] == "green" and x > 0):
                        x -= 1
                    elif (parcoursFusionne[x][y] == "yellow" and x < 2):
                        x += 1
                    elif (parcoursFusionne[x][y] == "darkblue" and y < 2):
                        y += 1
                    elif (parcoursFusionne[x][y] == "pink" and y > 0):
                        y -= 1
                    else:
                        continuer = False
                    print(x, y)
                    essai.append(parcoursFusionne[x][y])
                if (essai[-1] == "red"):
                    chemin = essai
        return chemin
