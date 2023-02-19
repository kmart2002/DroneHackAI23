#Script to connect drone cam to AI learning models
import cv2
from yolov5 import detectn

def main():
    # Connect to the Tello drone
    drone = tello.Tello()
    drone.connect()

    # Start the video stream
    drone.streamon()

    # Open a window to display the video stream
    cv2.namedWindow('Tello Video')

    # Main loop
    while True:
        # Get the latest video frame from the Tello camera
        frame = drone.get_frame_read().frame

        # Run object detection on the frame using YOLOv5
        # modify the detect() function to add changes to code
        # The function should take a single image frame as input and return the detected objects
        # The detected objects should be in the format expected by the YOLOv5 draw() function
        results = detect(frame)

        # Draw the detected objects on the frame
        # You can modify the draw() function to suit your needs
        # The function should take the original image frame and the detected objects as input, and draw the objects on the frame
        #frame = draw(frame, results)

        # Display the frame in the window
       # cv2.imshow('Tello Video', frame)
        #if cv2.waitKey(1) & 0xFF == ord('q'):
         #   break

    #loop to display the frame in the window
    #Iterate using the yolov5ImageCapture python file
    while True:
        image = drone.get_frame_read().frame
        image = cv2.resize(image, (360, 240))



        cv2.imshow("Image", image)
        cv2.waitKey(1)

    # Clean up, not needed, called elsewhere but could be called here once images are finished.
    #drone.land()
    #drone.quit()
   # cv2.destroyAllWindows()

