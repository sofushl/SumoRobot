import PicoRobotics
from utime import sleep_ms

board = PicoRobotics.KitronikPicoRobotics()

def Left(direction, power):
    board.motorOn(1,direction,power)
    board.motorOn(3,direction,power)

def Right(direction, power):
    board.motorOn(2,direction,power)
    board.motorOn(4,direction,power)
        
def stop():
    board.motorOff(1)
    board.motorOff(2)
    board.motorOff(3)
    board.motorOff(4)
    
def forward(time):
    Left("f", 1000)
    Right("f", 1000)
    sleep_ms(time)
    stop()

def reverse(time):
    Left("r", 1000)
    Right("r", 1000)
    sleep_ms(time)
    stop()

def turn(direction, time):
    if direction == "l":
        Left("r", 1000)
        Right("f", 1000)
        
    elif direction == "r":
        Left("f", 1000)
        Right("r", 1000)
        
    elif direction == "lf":
        Left("f", 25)
        Right("f", 1000)
        
    elif direction == "rf":
        Left("f", 1000)
        Right("f", 25)
    
    elif direction == "lr":
        Left("r", 25)
        Right("r", 1000)
        
    elif direction == "rr":
        Left("r", 1000)
        Right("r", 25)
        
    sleep_ms(time)
    stop()
    

def sensor(ang):
    board.servoWrite(1, ang)
