import asyncio

from marty_perso import MartyPerso

class MartysController:

    def __init__(self, marty1: MartyPerso, marty2: MartyPerso) -> None:
        self.marty1 = marty1
        self.marty2 = marty2

    def explorer_marty_1(self):
        self.grille1 = self.marty1.explorer()
        print(self.grille1)

    def explorer_marty_2(self):
        self.grille2 = self.marty2.explorer()
        print(self.grille2)