import cv2
import mediapipe as mp
import pyautogui
import math
import time

screen_w, screen_h = pyautogui.size()

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# smoothing
prev_x, prev_y = 0, 0
smooth = 7

paused = False
last_action = 0

def finger_up(lm, tip, pip):
    return lm[tip].y < lm[pip].y

with mp_hands.Hands(max_num_hands=1) as hands:
    while True:
        success, img = cap.read()
        if not success:
            break

        img = cv2.flip(img, 1)
        h, w, _ = img.shape
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(img_rgb)

        if result.multi_hand_landmarks:
            hand = result.multi_hand_landmarks[0]
            lm = hand.landmark

            index_up = finger_up(lm, 8, 6)
            middle_up = finger_up(lm, 12, 10)
            ring_up = finger_up(lm, 16, 14)
            pinky_up = finger_up(lm, 20, 18)

            ix, iy = int(lm[8].x * w), int(lm[8].y * h)
            tx, ty = int(lm[4].x * w), int(lm[4].y * h)
            mx, my = int(lm[12].x * w), int(lm[12].y * h)

            # Fist → pause / resume
            if not index_up and not middle_up and not ring_up and not pinky_up:
                if time.time() - last_action > 1:
                    paused = not paused
                    last_action = time.time()

            if not paused:
                # Smooth mouse move
                screen_x = screen_w * lm[8].x
                screen_y = screen_h * lm[8].y
                curr_x = prev_x + (screen_x - prev_x) / smooth
                curr_y = prev_y + (screen_y - prev_y) / smooth
                pyautogui.moveTo(curr_x, curr_y)
                prev_x, prev_y = curr_x, curr_y

                # Left click (thumb + index)
                if math.hypot(ix - tx, iy - ty) < 35:
                    pyautogui.click()
                    time.sleep(0.3)

                # Right click (index + middle pinch)
                if math.hypot(ix - mx, iy - my) < 35:
                    pyautogui.rightClick()
                    time.sleep(0.3)

                # Scroll (index + middle up)
                if index_up and middle_up and not ring_up:
                    pyautogui.scroll(-40)

            mp_draw.draw_landmarks(img, hand, mp_hands.HAND_CONNECTIONS)

        status = "PAUSED" if paused else "ACTIVE"
        cv2.putText(img, status, (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 0, 255) if paused else (0, 255, 0), 3)

        cv2.imshow("AI Virtual Mouse", img)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
