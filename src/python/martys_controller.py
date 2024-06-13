import asyncio
import threading

from ultraimport import ultraimport

from marty_perso import MartyPerso
Algo = ultraimport("__dir__/../python/algo.py", "Algo")
class MartysController:

    def __init__(self, marty1: MartyPerso, marty2: MartyPerso) -> None:
        self.marty1 = marty1
        self.marty2 = marty2
        self.verification_listes = False
        self.liste_fusionnee = True



    def start_validation(self):
        self.verification_listes = True
        self.thread_verification = threading.Thread(target=self.verification_liste)
        self.thread_verification.start()

    def verification_liste(self):
        while self.verification_listes:
            if self.grille1[0][0] != 0 and self.grille2[0][0] != 0:
                self.verification_listes = False
                self.liste_fusionnee = True
                algoObject = Algo(self.grille1, self.grille2)
                self.chemin_final = algoObject.getChemins()

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
                case "green":
                    self.marty1.move_forward(7)
                    self.marty1.stand_up()
                    break
                case "yellow":
                    self.marty1.move_backward(7)
                    self.marty1.stand_up()
                    break
                case "pink":
                    self.marty1.move_left(9)
                    break
                case "darkblue":
                    self.marty1.move_right(9)
                    break