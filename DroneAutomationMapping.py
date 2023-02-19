import cv2
from djitellopy import tello
import ManualOverrideModule as mo
import numpy as np
from time import sleep
import math

## PARAMETERS WE AR E WORKING WITH ##
# Need speed, angular speed, and from this we can calculate distance and how much angle we have

forwardSpeed = 100 / 10  # cm/s, traveled 117 cm in 10 seconds
angularSpeed = 360 / 10  # angular speed degrees/ second
interval = 0.25

# This will give us the distance and angle everytime we move one unit.
distanceInterval = forwardSpeed * interval
angularInterval = angularSpeed * interval

x, y = 500, 500
angle = 0
yaw = 0
# angle doesn't need to be reset to 0 because it will continue to add on from one point to another
mo.init()
# Initializing functions
ai = tello.Tello()
ai.connect()
print(ai.get_battery())

mappoints = [(0,0), (0,0)]


def getManualInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    distance = 0
    speed = 15
    angularSpeed = 50
    global x, y, yaw, angle

    # distance will reset because it won't add up, but will reset once it goes to another point

    # negative = left side
    if mo.keyPress("LEFT"):
        lr = -speed
        distance = distanceInterval
        angle = -180

    elif mo.keyPress("RIGHT"):
        lr = speed
        distance = -distanceInterval
        angle = 180

    if mo.keyPress("UP"):
        fb = speed
        distance = distanceInterval
        angle = 270

    elif mo.keyPress("DOWN"):
        fb = -speed
    distance = -distanceInterval
    angle = -90

    if mo.keyPress("w"):
        ud = speed
    elif mo.keyPress("s"):
        ud = -speed

    if mo.keyPress("a"):
        yv = -angularSpeed
        yaw -= angularInterval
        # will be added to our previous value rather than being a new value
    elif mo.keyPress("d"):
        yv = angularSpeed
    yaw += angularInterval

    if mo.keyPress("q"): q = ai.land()
    if mo.keyPress("e"): e = ai.takeoff()
    sleep(interval)
    angle += yaw
    x += int(distance * math.cos(math.radians(angle)))
    y += int(distance * math.sin(math.radians(angle)))

    return [lr, fb, ud, yv, x, y]


def dataPoints(image, mappoints):
    for mappoint in mappoints:
        cv2.circle(image, mappoint, 5, (0, 0, 255), cv2.FILLED)

        cv2.circle(image, mappoints[-1], 8, (255, 0, 0), cv2.FILLED)
    # CV2 does BGR not RGB
    cv2.putText(image, f'({(mappoints[-1][0] - 500) / 100},{(mappoints[-1][1] - 500) / 100})m',
                (mappoints[-1][0] + 10, mappoints[-1][1] + 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (255, 0, 255), 1)

    # starting position was 500, so we are subtracting 500 then dividing by 100 to get meters


while True:
    values = getManualInput()
    ai.send_rc_control(values[0], values[1], values[2], values[3])

    # Need numpy for mathematical calculations
    image = np.zeros((1000, 1000, 3), np.uint8)
    # unit = unsigned integers, 8 means 8 bit (2^8) values will range from 0 to 255
    # 3 channels (RGB channels)
    # plotImage is matrix of pixels; matrix of numbers
    if mappoints[-1][0] != values[4] or mappoints[-1][1] != values[5]:
        mappoints.append((values[4], values[5]))
    # creating a variable
    dataPoints(image, mappoints)
    cv2.imshow("Image Output", image)

    # Need a delay in the image output so --
    cv2.waitKey(1)
    # 1 millisecond
