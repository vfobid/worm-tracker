from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")  # Replace with trained worm model

def detect_worm_ai(frame):
    results = model(frame)
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2
            return (cx, cy), (x1, y1, x2, y2)
    return None, None

# To set up the environment, run the following commands in PowerShell:
#python -m venv .venv
#Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
#.\.venv\Scripts\Activate