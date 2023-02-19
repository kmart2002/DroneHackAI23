#Second attempt to connect drone livestream with object detection model

import cv2
import numpy as np
import time
import argparse
import torch
from yolov5.utils.datasets import LoadStreams
from yolov5.models.experimental import attempt_load
from yolov5.utils.general import check_img_size, non_max_suppression, scale_coords
from yolov5.utils.torch_utils import select_device

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--weights', type=str, default='yolov5s.pt', help='model.pt path')
parser.add_argument('--source', type=str, default='0', help='source')  # default camera source is 0
parser.add_argument('--conf-thres', type=float, default=0.25, help='object confidence threshold')
parser.add_argument('--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')
parser.add_argument('--img-size', type=int, default=200, help='inference size (pixels)')
opt = parser.parse_args()

# Set up the YOLOv5 model
device = select_device('')
model = attempt_load(opt.weights, map_location=device)
print(model.yaml)  # Add this line to print the model's YAML configuration

# Set up the camera source
cap = cv2.VideoCapture(opt.source)

# Start the video stream
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess the frame
    img = torch.from_numpy(frame).to(device)
    img = img.float() / 255.0
    img, _ = check_img_size(img, model.stride.max())

    # Detect objects using YOLOv5
    pred = model(img, augment=False)[0]
    pred = non_max_suppression(pred, opt.conf_thres, opt.iou_thres)

    # Process the detection results
    det = pred[0]
    if det is not None and len(det):
        det[:, :4] = scale_coords(img.shape[2:], det[:, :4], frame.shape).round()
        for *xyxy, conf, cls in reversed(det):
            label = f'{model.names[int(cls)]} {conf:.2f}'
            cv2.rectangle(frame, (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3])), (0, 255, 0), 2)
            cv2.putText(frame, label, (int(xyxy[0]), int(xyxy[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Display the results
    cv2.imshow('Object Detection', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
