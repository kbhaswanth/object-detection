from ultralytics import YOLO
import cv2

module = YOLO('../Yolo-weights/yolov8n.pt')
results = module("Images/1.png", show=True)
cv2.waitKey(0)
