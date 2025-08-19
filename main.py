import cv2
from config import VIDEO_PATH, USE_AI_DETECTION, FRAME_SKIP
from classical_tracker import detect_worm_cv
from ai_detector import detect_worm_ai
from utils import euclidean, draw_tracking

positions = []
total_distance = 0

cap = cv2.VideoCapture(VIDEO_PATH)
fps = cap.get(cv2.CAP_PROP_FPS)

frame_idx = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    if frame_idx % FRAME_SKIP != 0:
        frame_idx += 1
        continue

    detect_func = detect_worm_ai if USE_AI_DETECTION else detect_worm_cv
    center, box = detect_func(frame)

    if center:
        positions.append(center)
        if len(positions) >= 2:
            dist = euclidean(positions[-2], positions[-1])
            total_distance += dist

    frame = draw_tracking(frame, center, box)
    cv2.imshow("Worm Tracker", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    frame_idx += 1

cap.release()
cv2.destroyAllWindows()

total_time = (len(positions) * FRAME_SKIP) / fps
avg_speed = total_distance / total_time if total_time > 0 else 0

print(f"Average Speed (pixels/sec): {avg_speed:.2f}")