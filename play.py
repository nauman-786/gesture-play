import cv2
import mediapipe as mp
import pyautogui
import time

# --- INITIALIZATION ---
mp_hands = mp.solutions.hands
# Using a higher detection confidence to prevent "glitchy" movements
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8)
mp_draw = mp.solutions.drawing_utils

# Initialize Webcam
cap = cv2.VideoCapture(0)

# Variables for Swipe Logic
prev_x, prev_y = 0, 0
swipe_threshold = 70  # Distance in pixels to trigger a swipe
cooldown_time = 0.3    # Seconds to wait between swipes
last_swipe_time = time.time()

print("Camera loading... Click on the Subway Surfers window to start playing!")

# Create the window and force it to stay on top
cv2.namedWindow("Subway Surfers Controller", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Subway Surfers Controller", cv2.WND_PROP_TOPMOST, 1)

while cap.isOpened():
    success, img = cap.read()
    if not success:
        break

    # Flip image horizontally for a mirror effect (easier to control)
    img = cv2.flip(img, 1)
    h, w, c = img.shape
    
    # Convert BGR to RGB for MediaPipe
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Landmark 8 is the Index Finger Tip
            index_finger_tip = hand_landmarks.landmark[8]
            cx, cy = int(index_finger_tip.x * w), int(index_finger_tip.y * h)

            # Draw a purple circle on your finger tip
            cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            # Swipe Detection Logic
            current_time = time.time()
            if current_time - last_swipe_time > cooldown_time:
                dx = cx - prev_x
                dy = cy - prev_y

                # Horizontal Swipes (Left/Right)
                if abs(dx) > abs(dy) and abs(dx) > swipe_threshold:
                    if dx > 0:
                        pyautogui.press('right')
                        print("Swiped Right ->")
                    else:
                        pyautogui.press('left')
                        print("<- Swiped Left")
                    last_swipe_time = current_time

                # Vertical Swipes (Up/Down)
                elif abs(dy) > abs(dx) and abs(dy) > swipe_threshold:
                    if dy > 0:
                        pyautogui.press('down')
                        print("Swiped Down v")
                    else:
                        pyautogui.press('up')
                        print("Swiped Up ^")
                    last_swipe_time = current_time

            # Update previous coordinates
            prev_x, prev_y = cx, cy
            
            # Draw the hand skeleton for visual feedback
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display the Controller window
    cv2.putText(img, "AI CONTROLLER ACTIVE", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Subway Surfers Controller", img)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()