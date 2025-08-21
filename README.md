# Worm Tracker

A Python project for detecting and tracking worms in videos using **YOLOv8** (Ultralytics) or **OpenCV-based classical detection**.  
The tracker computes the **average worm speed (pixels/second)** from video recordings.

---

## Setup

Clone this repository and enter the folder:

git clone https://github.com/vfobid/worm-tracker.git
cd worm-tracker

Create a virtual environment and activate it in Powershell:

python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv310\Scripts\Activate

Install dependencies:

pip install -r requirements.txt


How to use:
Place your worm video in the project folder.

Download my trained YOLO model at: https://drive.google.com/file/d/1hlZHYGTG1hvS2VPUwCzBGoZ5hdhaVk42/view?usp=sharing

Open ai_tracker.py and set the path: model = YOLO("path_to_trained_YOLO_model")

Open config.py and set the path and options:

VIDEO_PATH = "your_video.mp4"   # path to your video
USE_AI_DETECTION = True         # True = YOLO, False = classical OpenCV
FRAME_SKIP = 2                  # skip frames for speed
Run the tracker:

python main.py
The script will:

Open a window showing tracking in real time

Print the average worm speed in pixels/sec to the terminal

Press Q to quit the video window.
