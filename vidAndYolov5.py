#Marty Kahn
#Code to apply object detection model on video file recieved
#Used in drone vid but can be used on any sort of video file

import cv2
import torch
import numpy as np
from pathlib import Path

# Load whichever model either pre-trained or custom
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Define video file path
video_path = Path('/Users/kmart/Desktop/Vids for training/droneObjectDetection.mp4')

# Initialize video capture
cap = cv2.VideoCapture(str(video_path))

# Define output video writer
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_path = video_path.with_name(f'{video_path.stem}_output.mp4')
out = cv2.VideoWriter(str(output_path), fourcc, fps, (width, height))

#Run loop while video is playing
while cap.isOpened():
    # Read frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert image to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Run detection(define size for this drone less than 300)
    results = model(frame, size=150)

    # Draw bounding boxes and labels on the image
    results.render()

    # Convert image back to BGR
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Write frame to output video
    out.write(frame)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
