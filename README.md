🏃‍♂️ AI Gesture-Controlled Subway Surfers
A Python-based AI controller that uses computer vision to track hand gestures and translate them into game commands.

🌟 How it Works
This project uses MediaPipe to track the coordinates of your index finger in real-time. When you swipe your hand, the script detects the movement and simulates an arrow key press to move the character in the game.

🛠️ Tech Stack
Python 3.12.7: The core programming language.

OpenCV: Handles the webcam video feed and image processing.

MediaPipe: Used for high-speed hand landmark detection.

PyAutoGUI: Sends virtual key presses to the game.

🚀 Quick Start
Clone the project:

Bash
git clone https://github.com/nauman-786/gesture-play.git
Install the required tools:

Bash
pip install opencv-python mediapipe==0.10.21 pyautogui
Run the game controller:

Bash
python play.py
🎮 Controls
Swipe Up: Jump

Swipe Down: Roll/Duck

Swipe Left/Right: Change lanes

Developed by Nauman Computer Science Student | Focused on AI and HCI


