import asyncio
import threading

from marty_perso import MartyPerso

class MartysController:

    def __init__(self, marty1: MartyPerso, marty2: MartyPerso) -> None:
        self.marty1 = marty1
        self.marty2 = marty2
        self.verification_listes = False
        self.liste_fusionnee = True

    def __fusion__(self, tab1, tab2):
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
        # TODO : appelle à la fonction pour obtenir le chemin le plus court
        self.chemin_final = tab3

    def start_validation(self):
        self.verification_listes = True
        self.thread_verification = threading.Thread(target=self.verification_liste)
        self.thread_verification.start()

    def verification_liste(self):
        while self.verification_listes:
            if self.grille1[0][0] != 0 and self.grille2[0][0] != 0:
                self.verification_listes = False
                self.liste_fusionnee = True
                self.__fusion__(self.grille1, self.grille2)

    def explorer_marty_1(self):
        self.grille1 = self.marty1.explorer()
        if not self.thread_verification.is_alive():
            self.start_validation()
        print(self.grille1)

    def explorer_marty_2(self):
        self.grille2 = self.marty2.explorer()
        if not self.thread_verification.is_alive():
            self.start_validation()
        print(self.grille2)

    def run_labyrinthe(self):
        if not self.liste_fusionnee:
            return False
        for instruction in self.chemin_final:
            match(instruction):
                case "nord":
                    self.marty1.move_forward(7)
                    break
                case "sud":
                    self.marty1.move_backward(7)
                    break
                case "ouest":
                    self.marty1.move_left(9)
                    break
                case "est":
                    self.marty1.move_right(9)
                    break