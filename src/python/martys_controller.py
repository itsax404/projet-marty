import asyncio
import threading

from ultraimport import ultraimport

from marty_perso import MartyPerso
Algo = ultraimport("__dir__/../python/algo.py", "Algo")
class MartysController:

    def __init__(self, marty1: MartyPerso, marty2: MartyPerso) -> None:
        self.marty1 = marty1
        self.marty2 = marty2

        self.grille1 = [[0 for _ in range(3)] for _ in range(3)]
        self.grille2 = [[0 for _ in range(3)] for _ in range(3)]

    def explorer(self):
        if self.marty1 is not None:
            self.explorer_marty_1()
        if self.marty1 is not None:
            self.explorer_marty_2()

    def explorer_marty_1(self):
        self.grille1 = self.marty1.explorer()
        print(self.grille1)

    def explorer_marty_2(self):
        self.grille2 = self.marty2.explorer()
        if not self.thread_verification.is_alive():
            self.start_validation()
        print(self.grille2)

    def run_labyrinthe(self):
        if self.grille1[0][0] == 0 or self.grille2[0][0]:
            return False
        algoObject = Algo(self.grille1, self.grille2)
        chemin_final = algoObject.getChemins()
        for instruction in chemin_final:
            match(instruction):
                case "green":
                    self.marty1.move_forward(7)
                    self.marty1.stand_up()
                    self.marty2.move_forward(7)
                    self.marty2.stand_up()
                    break
                case "yellow":
                    self.marty1.move_backward(7)
                    self.marty1.stand_up()
                    self.marty2.move_backward(7)
                    self.marty2.stand_up()
                    break
                case "pink":
                    self.marty1.move_left(6)
                    self.marty2.move_left(6)
                    break
                case "darkblue":
                    self.marty1.move_right(6)
                    self.marty2.move_right(6)
                    break