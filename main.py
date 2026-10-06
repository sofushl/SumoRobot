import PicoRobotics
from hcsr04 import HCSR04
from utime import sleep_ms as sleep
from machine import Pin, ADC
from neopixel import Neopixel
import Motor

board = PicoRobotics.KitronikPicoRobotics()
ssen = HCSR04(trigger_pin = 2, echo_pin = 3)
lsen = ADC(26)
button = Pin(0, Pin.IN)
pixel = Neopixel(1, 0, 28, "GRB")
reqdis = 90

def light(r,g,b):
    pixel.brightness(50)
    pixel.fill((r,g,b))
    pixel.show()

light(255,0,255)

def edge(i):
    line = lsen.read_u16()
    print(line)
    if line < 50000:
        light(255, 255, 0)
        Motor.reverse(400)
        distance = search()
        Motor.sensor(i)


def scan():
    for i in range(130,50,-20):
        Motor.sensor(i)
        distance = ssen.distance_cm()
        print(distance)
        if distance < reqdis:
            return True, distance, i
        sleep(120)
    Motor.sensor(130)
    return False, distance, False
    
def search():
    light(0, 255, 0)
    Motor.turn("l", 700)
    light(0,0,255)
    while True:
        target, distance, direction = scan()
        if target:
            if direction != 0:
                light(255,100,0)
                if direction == 50:
                    Motor.turn("l",200)
                elif direction == 70:
                    Motor.turn("l",100)
                elif direction == 110:
                    Motor.turn("r",100)
                elif direction == 130:
                    Motor.turn("r",200)
            return distance
        Motor.turn("l",300)
    
def livescan():
    for i in [50,130]:
        edge(i)
        
        light(255,0,0)
        Motor.sensor(i)
        distance = ssen.distance_cm()
        print(distance)
        if distance < reqdis:
            if i == 50:
                Motor.turn("lf",120)
            elif i == 130:
                Motor.turn("rf",120)
            else:
                Motor.forward(120)
        else:
            Motor.forward(120)
            

        



while True:
    if button.value() == 0:   
        break
    sleep(10)
light(0,100,255)
sleep(3000)

distance = search()

while True:
    livescan()
    if button.value() == 0:
        Motor.stop()
        break