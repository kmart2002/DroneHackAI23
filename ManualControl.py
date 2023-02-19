from djitellopy import tello
import ManualOverrideModule as mo
from time import sleep


mo.init()
# Initializing functions
ai = tello.Tello()
ai.connect()
print(ai.get_battery())

def getManualInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    # negative = left side
    if mo.keyPress("LEFT"): lr = -speed
    elif mo.keyPress("RIGHT"): lr = speed

    if mo.keyPress("UP"): fb = speed
    elif mo.keyPress("DOWN"): fb = -speed

    if mo.keyPress("w"): ud = speed
    elif mo.keyPress("s"): ud = -speed

    if mo.keyPress("a"): yv = speed
    elif mo.keyPress("d"): yv = -speed

    if mo.keyPress("q"): q = ai.land()
    if mo.keyPress("e"): e = ai.takeoff()

    return [lr, fb, ud, yv]

while True:
    values = getManualInput()
    ai.send_rc_control(values[0], values[1], values[2], values[3])
    sleep(0.5)


