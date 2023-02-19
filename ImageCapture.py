from djitellopy import tello
import cv2
# imported cv2 (openCV) for computer vision, image and processing.

# want to add delays for each command (line 2)

# Need to connect to Tello Drone, create tello object

ai = tello.Tello()
# this will create the tello object.
ai.connect()
# connecting to Tello Drone

# To make sure this code is running, I'll print out the battery percentage to see if the connection is stable

print(ai.get_battery())

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




