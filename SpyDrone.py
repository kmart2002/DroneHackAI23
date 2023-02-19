from djitellopy import tello
import ManualOverrideModule as mo
import time
import cv2

mo.init()
# Initializing functions
ai = tello.Tello()
ai.connect()
print(ai.get_battery())
global image

ai.streamon()


def getManualInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if mo.keyPress('p'):
        cv2.imwrite(f'Drone/Images/{time.time()}.jpg', image)
        # Want to make sure there is a unique name everytime so images don't override each other
        time.sleep(0.5)

    # negative = left side
    if mo.keyPress("LEFT"): lr = -speed
    elif mo.keyPress("RIGHT"):lr = speed

    if mo.keyPress("UP"): fb = speed
    elif mo.keyPress("DOWN"):fb = -speed

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

    image = ai.get_frame_read().frame
    image = cv2.resize(image, (360, 240))
    cv2.imshow("Image", image)
    cv2.waitKey(1)







