import cv2
import mediapipe as mp
import numpy as np
import math

# Khởi tạo MediaPipe
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Mở webcam
cap = cv2.VideoCapture(0)

# Ngưỡng khoảng cách để xác định Grab
GRAB_THRESHOLD = 40  

# Trạng thái
is_grabbing = False

def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    h, w, _ = img.shape

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    status_text = "No Hand"

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            # Lấy tọa độ ngón cái (4) và ngón trỏ (8)
            thumb = handLms.landmark[4]
            index = handLms.landmark[8]

            thumb_pos = (int(thumb.x * w), int(thumb.y * h))
            index_pos = (int(index.x * w), int(index.y * h))

            # Vẽ điểm
            cv2.circle(img, thumb_pos, 10, (255, 0, 0), -1)
            cv2.circle(img, index_pos, 10, (0, 255, 0), -1)

            # Tính khoảng cách
            dist = distance(thumb_pos, index_pos)

            if dist < GRAB_THRESHOLD:
                is_grabbing = True
                status_text = "GRAB / DRAG"
            else:
                if is_grabbing:
                    status_text = "DROP"
                else:
                    status_text = "MOVE"
                is_grabbing = False

            # Hiển thị khoảng cách
            cv2.putText(img, f"Distance: {int(dist)}",
                        (20, 60), cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (255, 255, 0), 2)

    # Hiển thị trạng thái
    cv2.putText(img, f"Status: {status_text}",
                (20, 100), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 3)

    cv2.imshow("Hand Gesture - Drag & Drop", img)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC để thoát
        break

cap.release()
cv2.destroyAllWindows()
