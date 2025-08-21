import math
import cv2

def euclidean(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def draw_tracking(frame, center, box):
    if box:
        cv2.rectangle(frame, box[:2], box[2:], (0, 255, 0), 2)
    if center:
        cv2.circle(frame, center, 5, (0, 0, 255), -1)
    return frame