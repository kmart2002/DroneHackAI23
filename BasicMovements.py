from djitellopy import tello
import cv2
from time import sleep

# want to add delays for each command (line 2)

# Need to connect to Tello Drone, create tello object

ai = tello.Tello()
# this will create the tello object.
ai.connect()
# connecting to Tello Drone

# To make sure this code is running, I'll print out the battery percentage to see if the connection is stable

print(ai.get_battery())

# Needs to take off

ai.takeoff()

# Automating the drone to go forward at a velocity of 50

ai.send_rc_control(0, 50, 0, 0)

"""Send RC control via four channels. Command is sent every self.TIME_BTW_RC_CONTROL_COMMANDS seconds.
        Arguments:
            left_right_velocity: -100~100 (left/right)
            forward_backward_velocity: -100~100 (forward/backward)
            up_down_velocity: -100~100 (up/down)
            yaw_velocity: -100~100 (yaw)
        """
sleep(2)
# delays per second, how long it stays in the air
ai.send_rc_control(0, 0, 0, 25)
sleep(2)
# Rotates right at 50
ai.send_rc_control(0, 75, 0, 0)
sleep(2)
# Goes forward at a velocity of 50 again

ai.send_rc_control(0, 0, 0, 0)
# Need this so the drone stops and then lands
ai.land()

# For Computer Vision
ai.streamon()
# Gives us all the frames that we need

while True:
    image = ai.get_frame_read().frame
    # This should give us each image one by one (individually)
    # To resize image we can use the ML library openCV2 to do such
    image = cv2.resize(image, (360, 240))
    # Keeping the size of the frame small so the image loads faster
    # image then updates into the resized because of CV2 library

    cv2.imshow("Image", image)
    # Creates a window to display image

    cv2.waitKey(1)
    """Frames will shut down, before we can see it, so we need to give it a delay of some sort, 1 milisecond should
    do the trick. There will be a delay in the frames,because of the transfer from drone to client side, 
    trying to keep up with the graphical computations."""
