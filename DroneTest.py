from djitellopy import tello
from time import sleep

ai = tello.Tello()
# this will create the tello object.
ai.connect()
# connecting to Tello Drone

# To make sure this code is running, I'll print out the battery percentage to see if the connection is stable

print(ai.get_battery())
