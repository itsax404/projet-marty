from martypy import Marty


class MartyPerso:
    def __init__(self):
        self.marty = Marty("wifi", "192.168.0.103")

    def setIP(self, ip):
        self.marty = Marty("wifi", ip)

    def connect(self):
        return

    def disconnect(self):
        self.marty.close()

    def move_forward(self):
        self.marty.walk(2)

    def move_backward(self):
        self.marty.walk(-2)

    def move_left(self):
        self.marty.sidestep("left")

    def move_right(self):
        self.marty.sidestep("right")

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
        self.marty.eyes("normal")

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

    def get_color_sensor(self):
        return str(self.marty.get_color_sensor_hex("left"))

    def is_connected(self):
        return self.marty.is_conn_ready()

