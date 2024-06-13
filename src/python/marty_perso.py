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
        hex_color = str(self.marty.get_color_sensor_hex("LeftColorSensor"))
        red_value = int(hex_color[0:2], 16)
        green_value = int(hex_color[2:4], 16)
        blue_value = int(hex_color[4:6], 16)

        red_value = int(red_value * 160/100)
        if(red_value > 255):
            n = red_value - 255
            red_value -= n
        green_value = int(green_value * 260/100)
        if(green_value > 255):
            n = green_value - 255
            green_value -= n
        blue_value = int(blue_value * 260/100)
        if(blue_value > 255):
            n = blue_value - 255
            blue_value -= n

        if((red_value > 130) and (green_value > 20 and green_value < 60) and (blue_value > 20 and blue_value < 60)):
            return "red"

        elif((red_value > 50 and red_value < 100) and (green_value > 50) and (blue_value > 40 and blue_value < 60)):
            return "green"
            
        elif((red_value > 70 and red_value < 125 ) and (green_value > 100 and green_value < 155) and (blue_value > 130)):
            return "blue"
            
        elif((red_value > 50 and red_value < 100) and (green_value > 0 and green_value < 60) and (blue_value > 50 and blue_value < 120)):
            return "purple"
            
        elif((red_value > 200) and (green_value > 180 and green_value < 220) and (blue_value > 100 and blue_value < 130)):
            return "yellow"
            
        elif((red_value > 200) and (green_value > 200) and (blue_value > 200)):
            return "white"

        elif((red_value < 30) and (green_value < 30) and (blue_value < 30)):
            return "black"
        
        elif((red_value > 170 and red_value < 190) and (green_value > 50 and green_value < 70) and (blue_value > 80 and blue_value < 100)):
            return "pink"
            
        else:
            return "unknown"

    def explorer(self):
        grille = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            if i % 2 == 0:
                for j in range(3):
                    if j != 0:
                        self.move_forward(7)
                    sleep(500)
                    color = self.get_color_sensor()
                    print(f"i : {i} | j : {j} | color : {color}")
                    grille[i][j] = color
            else:
                for j in range(2, -1, -1):
                    if j != 2:
                        self.move_backward(7)
                    sleep(500)
                    color = self.get_color_sensor()
                    print(f"i : {i} | j : {j} | color : {color}")
                    grille[i][j] = color
            if i < 2:
                self.move_left(5)
                sleep(500)
                print("gauche")
        return grille


    def is_connected(self):
        if self.marty is None:
            return False
        return self.marty.is_conn_ready()

