#Rahul Nalam
#Code used to display graphically stream from the drone

from djitellopy import tello
import cv2
import yolov5



#ai is the address of the drone
ai = tello.Tello()
ai.connect()
#print battery level and start stream
print(ai.get_battery())
ai.streamon()
#Read frames while stream is on
while True:
   image = ai.get_frame_read().frame
   image = cv2.resize(image, (360, 240))


   cv2.imshow("Image", image)
   cv2.waitKey(1)
