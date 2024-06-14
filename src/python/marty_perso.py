import time
from asyncio import sleep

from martypy import Marty


class MartyPerso:
    def __init__(self, name):
        self.marty = None
        self.name = name

    def setIP(self, ip):
        self.marty = Marty("wifi", ip)

    def connect(self):
        return

    def disconnect(self):
        self.marty.close()

    def move_forward(self, steps=2):
        self.marty.walk(steps, 'auto', 0)

    def move_backward(self, steps=2):
        self.marty.walk(steps, step_length=-20)

    def move_left(self, steps=1):
        self.marty.sidestep("left", steps=steps)

    def move_right(self, steps=1):
        self.marty.sidestep("right", steps=steps)

    def turn_left(self):
        self.marty.walk(2, turn=15)

    def turn_right(self):
        self.marty.walk(2, turn=-15)

    def stop(self):
        self.marty.stop()

    def dance(self):
        self.marty.dance()

    def circular_dance(self):
        self.marty.circle_dance()

    def kick(self):
        self.marty.kick()

    def eyes(self):
        self.marty.eyes("excited")

    def celebrate(self):
        self.marty.celebrate()

    def wiggle_eyes(self):
        self.marty.wiggle()

    def stand_up(self):
        self.marty.stand_straight()

    def get_battery_level(self):
        return str(self.marty.get_battery_remaining())

    def get_distance(self):
        return str(self.marty.get_distance_sensor())

    def get_name(self):
        return self.name

    def get_color_sensor(self):
        dict_tolerance_color1 = {'red_ratio': 1.1, 'green_ratio': 1.9, 'blue_ratio': 2.5, 'red': {'red_min': 130, 'red_max': 256, 'green_min': 20, 'green_max': 60, 'blue_min': 30, 'blue_max': 70}, 'green': {'red_min': 50, 'red_max': 100, 'green_min': 50, 'green_max': 255, 'blue_min': 55, 'blue_max': 90}, 'darkblue': {'red_min': 35, 'red_max': 60, 'green_min': 35, 'green_max': 70, 'blue_min': 55, 'blue_max': 90}, 'lightblue': {'red_min': 80, 'red_max': 115, 'green_min': 150, 'green_max': 175, 'blue_min': 
195, 'blue_max': 256}, 'yellow': {'red_min': 10, 'red_max': 30, 'green_min': 180, 'green_max': 256, 'blue_min': 100, 'blue_max': 256}, 'white': {'red_min': 200, 'red_max': 256, 'green_min': 200, 'green_max': 256, 'blue_min': 200, 'blue_max': 256}, 'black': {'red_min': 0, 'red_max': 40, 'green_min': 0, 'green_max': 30, 'blue_min': 0, 'blue_max': 30}, 'pink': {'red_min': 170, 'red_max': 190, 'green_min': 50, 'green_max': 70, 'blue_min': 80, 'blue_max': 120}}
        dict_tolerance_color2 = {}
        if self.name.lower() == "marty1":
            color =  self.__get_color__sensor__(dict_tolerance_color1)
            print(color)
            return color    
        else:
            color =  self.__get_color__sensor__(dict_tolerance_color2)
            print(color)
            return color

    def __get_color__sensor__(self, dict_tolerance_color):
        hex_color = str(self.marty.get_color_sensor_hex("LeftColorSensor"))
        red_value = int(hex_color[0:2], 16)
        green_value = int(hex_color[2:4], 16)
        blue_value = int(hex_color[4:6], 16)

        red_ratio = dict_tolerance_color["red_ratio"]
        blue_ratio = dict_tolerance_color["blue_ratio"]
        green_ratio = dict_tolerance_color["green_ratio"]

        red_value = int(red_value * red_ratio)
        if (red_value > 255):
            n = red_value - 255
            red_value -= n
        green_value = int(green_value * green_ratio)
        if (green_value > 255):
            n = green_value - 255
            green_value -= n
        blue_value = int(blue_value * blue_ratio)
        if (blue_value > 255):
            n = blue_value - 255
            blue_value -= n

        if (dict_tolerance_color["red"]["red_min"] < red_value < dict_tolerance_color["red"]["red_max"]) and (
                dict_tolerance_color["red"]["green_min"] < green_value < dict_tolerance_color["red"]["green_max"]) and (
                dict_tolerance_color["red"]["blue_min"] < blue_value < dict_tolerance_color["red"]["blue_max"]):
            return "red"

        elif (dict_tolerance_color["green"]["red_min"] < red_value < dict_tolerance_color["green"]["red_max"]) and (
                dict_tolerance_color["green"]["green_min"] < green_value < dict_tolerance_color["green"][
            "green_max"]) and (
                dict_tolerance_color["green"]["blue_min"] < blue_value < dict_tolerance_color["green"]["blue_max"]):
            return "green"

        elif (dict_tolerance_color["darkblue"]["red_min"] < red_value < dict_tolerance_color["darkblue"][
            "red_max"]) and (
                dict_tolerance_color["darkblue"]["green_min"] < green_value < dict_tolerance_color["darkblue"][
            "green_max"]) and (
                dict_tolerance_color["darkblue"]["blue_min"] < blue_value < dict_tolerance_color["darkblue"][
            "blue_max"]):
            return "darkblue"

        elif (dict_tolerance_color["lightblue"]["red_min"] < red_value < dict_tolerance_color["lightblue"][
            "red_max"]) and (
                dict_tolerance_color["lightblue"]["green_min"] < green_value < dict_tolerance_color["lightblue"][
            "green_max"]) and (
                dict_tolerance_color["lightblue"]["blue_min"] < blue_value < dict_tolerance_color["lightblue"][
            "blue_max"]):
            return "lightblue"

        elif (dict_tolerance_color["yellow"]["red_min"] < red_value < dict_tolerance_color["yellow"]["red_max"]) and (
                dict_tolerance_color["yellow"]["green_min"] < green_value < dict_tolerance_color["yellow"][
            "green_max"]) and (
                dict_tolerance_color["yellow"]["blue_min"] < blue_value < dict_tolerance_color["yellow"]["blue_max"]):
            return "yellow"

        elif (dict_tolerance_color["white"]["red_min"] < red_value < dict_tolerance_color["white"]["red_max"]) and (
                dict_tolerance_color["white"]["green_min"] < green_value < dict_tolerance_color["white"][
            "green_max"]) and (
                dict_tolerance_color["white"]["blue_min"] < blue_value < dict_tolerance_color["white"]["blue_max"]):
            return "white"

        elif (dict_tolerance_color["black"]["red_min"] < red_value < dict_tolerance_color["black"]["red_max"]) and (
                dict_tolerance_color["black"]["green_min"] < green_value < dict_tolerance_color["black"][
            "green_max"]) and (
                dict_tolerance_color["black"]["blue_min"] < blue_value < dict_tolerance_color["black"]["blue_max"]):
            return "black"

        elif (dict_tolerance_color["pink"]["red_min"] < red_value < dict_tolerance_color["pink"]["red_max"]) and (
                dict_tolerance_color["pink"]["green_min"] < green_value < dict_tolerance_color["pink"][
            "green_max"]) and (
                dict_tolerance_color["pink"]["blue_min"] < blue_value < dict_tolerance_color["pink"]["blue_max"]):
            return "pink"

        else:
            return "unknown"

    def explorer(self):
        print("explorer")
        self.marty.stand_straight()
        grille = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            print("a")
            if i % 2 == 0:
                print("b")
                for j in range(3):
                    print("c")
                    if j != 0:
                        self.move_forward(7)
                        self.marty.stand_straight()
                    print("d")
                    time.sleep(0.5)
                    color = self.get_color_sensor()
                    print(f"i : {i} | j : {j} | color : {color}")
                    grille[i][j] = color
            else:
                for j in range(2, -1, -1):
                    if j != 2:
                        self.move_backward(7)
                        self.stand_up()
                    time.sleep(0.5)
                    color = self.get_color_sensor()
                    print(f"i : {i} | j : {j} | color : {color}")
                    grille[i][j] = color
            if i < 2:
                self.move_left(5)
                self.stand_up()
                time.sleep(0.5)
                print("gauche")
        return grille


    def is_connected(self):
        if self.marty is None:
            return False
        return self.marty.is_conn_ready()

