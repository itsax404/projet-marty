import cv2
from asyncio import sleep
from martypy import Marty
from PIL import Image

# Fonction pour créer une image d'une seule couleur
def creer_image_couleur(rgb, taille=(100, 100)):
    image = Image.new("RGB", taille, rgb)
    image.show()

marty = Marty("wifi","192.168.0.102")
marty.set_blocking(False)


marty.stand_straight()
hex_color = str(marty.get_color_sensor_hex("LeftColorSensor"))
red_value = int(hex_color[0:2], 16)
print(f"Hex value : {hex_color[0:2]}")
green_value = int(hex_color[2:4], 16)
blue_value = int(hex_color[4:6], 16)
print(f"Red: {red_value} | Green: {green_value} | Blue: {blue_value}")

rgb = (red_value, green_value, blue_value)  
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
print(f"Red: {red_value} | Green: {green_value} | Blue: {blue_value}")
rgb = (red_value, green_value,blue_value)

if((red_value > 130) and (green_value > 20 and green_value < 60) and (blue_value > 20 and blue_value < 60)):
    print("red")

elif((red_value > 50 and red_value < 100) and (green_value > 50) and (blue_value > 40 and blue_value < 60)):
    print("green")
    
elif((red_value > 40 and red_value < 50 ) and (green_value > 40 and green_value < 50) and (blue_value > 60 and blue_value < 70)):
    print("darkblue")
    
elif((red_value > 100 and red_value < 110) and (green_value > 160 and green_value < 170) and (blue_value > 200 and blue_value < 210)):
    print("lightblue")
    
elif((red_value > 200) and (green_value > 180 and green_value < 220) and (blue_value > 100 and blue_value < 130)):
    print("yellow")
    
elif((red_value > 200) and (green_value > 200) and (blue_value > 200)):
    print("white")

elif((red_value < 30) and (green_value < 30) and (blue_value < 30)):
    print("black")
elif((red_value > 170 and red_value < 190) and (green_value > 50 and green_value < 70) and (blue_value > 80 and blue_value < 100)):
    print("pink")
else:
    print("unknown")