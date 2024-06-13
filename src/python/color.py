import cv2
from asyncio import sleep
from martypy import Marty

# Fonction pour créer une image d'une seule couleur

marty = Marty("wifi", "192.168.0.102")
marty.set_blocking(False)

dict_tolerance_color = {
    "red_ratio": 160 / 100,
    "green_ratio": 240 / 100,
    "blue_ratio": 250 / 100,
    "red": {"red_min": 130, "red_max": 255, "green_min": 20, "green_max": 60, "blue_min": 30, "blue_max": 70},
    "green": {"red_min": 50, "red_max": 100, "green_min": 50, "green_max": 255, "blue_min": 55, "blue_max": 90},
    "darkblue": {"red_min": 35, "red_max": 60, "green_min": 35, "green_max": 70, "blue_min": 55, "blue_max": 90},
    "lightblue": {"red_min": 80, "red_max": 115, "green_min": 150, "green_max": 175, "blue_min": 195, "blue_max": 230},
    "yellow": {"red_min": 200, "red_max": 255, "green_min": 180, "green_max": 230, "blue_min": 100, "blue_max": 130},
    "white": {"red_min": 200, "red_max": 255, "green_min": 200, "green_max": 255, "blue_min": 200, "blue_max": 255},
    "black": {"red_min": 0, "red_max": 40, "green_min": 0, "green_max": 30, "blue_min": 0, "blue_max": 30},
    "pink": {"red_min": 170, "red_max": 190, "green_min": 50, "green_max": 70, "blue_min": 80, "blue_max": 120},
}

marty.stand_straight()
hex_color = str(marty.get_color_sensor_hex("LeftColorSensor"))
red_value = int(hex_color[0:2], 16)
print(f"Hex value : {hex_color[0:2]}")
green_value = int(hex_color[2:4], 16)
blue_value = int(hex_color[4:6], 16)
print(f"Red: {red_value} | Green: {green_value} | Blue: {blue_value}")

rgb = (red_value, green_value, blue_value)
red_value = int(red_value * dict_tolerance_color["red_ratio"])
if (red_value > 255):
    n = red_value - 255
    red_value -= n
green_value = int(green_value * dict_tolerance_color["green_ratio"])
if (green_value > 255):
    n = green_value - 255
    green_value -= n
blue_value = int(blue_value * dict_tolerance_color["blue_ratio"])
if (blue_value > 255):
    n = blue_value - 255
    blue_value -= n
print(f"Red: {red_value} | Green: {green_value} | Blue: {blue_value}")
rgb = (red_value, green_value, blue_value)

if (dict_tolerance_color["red"]["red_min"] < red_value < dict_tolerance_color["red"]["red_max"]) and (
        dict_tolerance_color["red"]["green_min"] < green_value < dict_tolerance_color["red"]["green_max"]) and (
        dict_tolerance_color["red"]["blue_min"] < blue_value < dict_tolerance_color["red"]["blue_max"]):
    print("red")

elif (dict_tolerance_color["green"]["red_min"] < red_value < dict_tolerance_color["green"]["red_max"]) and (
        dict_tolerance_color["green"]["green_min"] < green_value < dict_tolerance_color["green"]["green_max"]) and (
        dict_tolerance_color["green"]["blue_min"] < blue_value < dict_tolerance_color["green"]["blue_max"]):
    print("green")

elif (dict_tolerance_color["darkblue"]["red_min"] < red_value < dict_tolerance_color["darkblue"]["red_max"]) and (
        dict_tolerance_color["darkblue"]["green_min"] < green_value < dict_tolerance_color["darkblue"][
    "green_max"]) and (
        dict_tolerance_color["darkblue"]["blue_min"] < blue_value < dict_tolerance_color["darkblue"]["blue_max"]):
    print("darkblue")

elif (dict_tolerance_color["lightblue"]["red_min"] < red_value < dict_tolerance_color["lightblue"]["red_max"]) and (
        dict_tolerance_color["lightblue"]["green_min"] < green_value < dict_tolerance_color["lightblue"][
    "green_max"]) and (
        dict_tolerance_color["lightblue"]["blue_min"] < blue_value < dict_tolerance_color["lightblue"]["blue_max"]):
    print("lightblue")

elif (dict_tolerance_color["yellow"]["red_min"] < red_value < dict_tolerance_color["yellow"]["red_max"]) and (
        dict_tolerance_color["yellow"]["green_min"] < green_value < dict_tolerance_color["yellow"]["green_max"]) and (
        dict_tolerance_color["yellow"]["blue_min"] < blue_value < dict_tolerance_color["yellow"]["blue_max"]):
    print("yellow")

elif (dict_tolerance_color["white"]["red_min"] < red_value < dict_tolerance_color["white"]["red_max"]) and (
        dict_tolerance_color["white"]["green_min"] < green_value < dict_tolerance_color["white"]["green_max"]) and (
        dict_tolerance_color["white"]["blue_min"] < blue_value < dict_tolerance_color["white"]["blue_max"]):
    print("white")

elif (dict_tolerance_color["black"]["red_min"] < red_value < dict_tolerance_color["black"]["red_max"]) and (
        dict_tolerance_color["black"]["green_min"] < green_value < dict_tolerance_color["black"]["green_max"]) and (
        dict_tolerance_color["black"]["blue_min"] < blue_value < dict_tolerance_color["black"]["blue_max"]):
    print("black")

elif (dict_tolerance_color["pink"]["red_min"] < red_value < dict_tolerance_color["pink"]["red_max"]) and (
        dict_tolerance_color["pink"]["green_min"] < green_value < dict_tolerance_color["pink"]["green_max"]) and (
        dict_tolerance_color["pink"]["blue_min"] < blue_value < dict_tolerance_color["pink"]["blue_max"]):
    print("pink")

else:
    print("unknown")

print(dict_tolerance_color)
