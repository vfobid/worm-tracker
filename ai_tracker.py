from ultralytics import YOLO
import cv2

model = YOLO("runs/detect/train2/weights/best.pt")  #trained worm model

def detect_worm_ai(frame):
    results = model(frame)
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2
            return (cx, cy), (x1, y1, x2, y2)
    return None, None

