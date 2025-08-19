import cv2
import os
import random
import shutil

# ---------------- CONFIG ----------------
video_path = "sample_video/worm.mp4"   # your input video
dataset_folder = "worm_dataset"        # output YOLO dataset
interval = 0.5                         # seconds between frames
splits = {"train": 0.7, "val": 0.2, "test": 0.1}
# ----------------------------------------


def extract_frames(video_path, temp_folder, interval=2):
    """Extract frames every `interval` seconds from a video."""
    os.makedirs(temp_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise IOError(f"Cannot open video {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * interval)

    count = 0
    saved = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if count % frame_interval == 0:
            frame_name = os.path.join(temp_folder, f"frame_{saved:05d}.jpg")
            cv2.imwrite(frame_name, frame)
            saved += 1

        count += 1

    cap.release()
    return saved


def prepare_yolo_dataset(temp_folder, dataset_folder, splits):
    """Split extracted frames into YOLO dataset structure with empty label files."""
    # Create dataset structure
    for split in splits:
        os.makedirs(os.path.join(dataset_folder, "images", split), exist_ok=True)
        os.makedirs(os.path.join(dataset_folder, "labels", split), exist_ok=True)

    frames = [f for f in os.listdir(temp_folder) if f.endswith(".jpg")]
    random.shuffle(frames)

    n = len(frames)
    train_end = int(n * splits["train"])
    val_end = train_end + int(n * splits["val"])

    for i, frame in enumerate(frames):
        if i < train_end:
            split = "train"
        elif i < val_end:
            split = "val"
        else:
            split = "test"

        # Copy image
        src_img = os.path.join(temp_folder, frame)
        dst_img = os.path.join(dataset_folder, "images", split, frame)
        shutil.copy(src_img, dst_img)

        # Create empty label file
        label_name = os.path.splitext(frame)[0] + ".txt"
        label_path = os.path.join(dataset_folder, "labels", split, label_name)
        with open(label_path, "w") as f:
            pass  # empty for now, to be filled by labeling tool


if __name__ == "__main__":
    temp_folder = "temp_frames"

    print("Extracting frames...")
    total = extract_frames(video_path, temp_folder, interval)
    print(f"✅ Extracted {total} frames")

    print("Preparing YOLO dataset structure...")
    prepare_yolo_dataset(temp_folder, dataset_folder, splits)
    print(f"✅ YOLO dataset ready in '{dataset_folder}'")

    # Optional: clean up temp frames
    shutil.rmtree(temp_folder)
    print("✅ Temporary frames cleaned up")