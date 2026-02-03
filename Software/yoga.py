import cv2
import mediapipe as mp
import time
import sys
import pygame
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Ініціалізація Mediapipe Pose
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose()

# Ініціалізація для звуку
pygame.mixer.init()
SOUND_FILE = "correct.wav"
success_sound = pygame.mixer.Sound(SOUND_FILE) if pygame.mixer.get_init() else None
last_sound_time = 0
SOUND_COOLDOWN = 3

# Ініціалізація шрифту
FONT_PATH = "C:/Windows/Fonts/arial.ttf"
try:
    font = ImageFont.truetype(FONT_PATH, 20)
except IOError:
    print(f"Помилка: не вдалося завантажити шрифт {FONT_PATH}")
    font = None

# Список поз
poses = ["pose1.jpg", "pose2.jpg", "pose3.jpg", "pose4.jpg"]
pose_index = 0
goodbye_image = cv2.imread("goodbye.jpg")
show_skeleton = True


# Завантаження зображення
def load_pose_image(index):
    img = cv2.imread(poses[index], cv2.IMREAD_UNCHANGED)
    if img is None:
        print(f"Помилка: не вдалося завантажити {poses[index]}")
    return img


overlay_image = load_pose_image(pose_index)

# Координати кнопок
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 50
buttons = {
    "Наступна поза": (1050, 430),
    "Попередня поза": (1050, 500),
    "Скелет": (1050, 570),
    "Вихід": (1050, 640)
}

button_press_time = {key: None for key in buttons}
pose_check_time = None


def check_button_press(x, y, button_name):
    bx, by = buttons[button_name]
    return (bx <= x <= bx + BUTTON_WIDTH) and (by <= y <= by + BUTTON_HEIGHT)


def show_goodbye_and_exit(frame):
    if goodbye_image is not None:
        h, w = frame.shape[:2]
        gh, gw = goodbye_image.shape[:2]
        x = (w - gw) // 2
        y = (h - gh) // 2
        frame[y:y + gh, x:x + gw] = goodbye_image
        cv2.imshow('Mediapipe Yoga', frame)
        cv2.waitKey(3000)
    cv2.destroyAllWindows()
    sys.exit()


def check_current_pose(landmarks, pose_number, h, w):
    global pose_check_time, last_sound_time

    current_time = time.time()
    is_correct = False

    if pose_number == 0:
        # П'ятка вище протилежного коліна
        heel_above = (
                landmarks[mp_pose.PoseLandmark.LEFT_HEEL].y < landmarks[mp_pose.PoseLandmark.RIGHT_KNEE].y or
                landmarks[mp_pose.PoseLandmark.RIGHT_HEEL].y < landmarks[mp_pose.PoseLandmark.LEFT_KNEE].y
        )
        # Лікті вище плечей
        elbows_above = (
                landmarks[mp_pose.PoseLandmark.LEFT_ELBOW].y < landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].y and
                landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW].y < landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER].y
        )
        is_correct = heel_above and elbows_above

    elif pose_number == 1:
        # Пальці ніг ширше тазу
        toes_width = abs(
            landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX].x -
            landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].x
        ) > 0.15
        # Лікті вище плечей
        elbows_above = (
                landmarks[mp_pose.PoseLandmark.LEFT_ELBOW].y < landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].y and
                landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW].y < landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER].y
        )
        is_correct = toes_width and elbows_above

    elif pose_number == 2:
        # Пальці ніг ширше тазу
        toes_width = abs(
            landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX].x -
            landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].x
        ) > 0.15
        # Пальці руки правіше п'ятки
        hand_foot = (
                landmarks[mp_pose.PoseLandmark.RIGHT_INDEX].x > landmarks[mp_pose.PoseLandmark.RIGHT_HEEL].x or
                landmarks[mp_pose.PoseLandmark.LEFT_INDEX].x > landmarks[mp_pose.PoseLandmark.LEFT_HEEL].x
        )
        is_correct = toes_width and hand_foot

    elif pose_number == 3:
        # Таз вище плечей
        hips_y = (
                         landmarks[mp_pose.PoseLandmark.LEFT_HIP].y +
                         landmarks[mp_pose.PoseLandmark.RIGHT_HIP].y
                 ) / 2
        shoulders_y = (
                              landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].y +
                              landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER].y
                      ) / 2
        is_correct = hips_y < shoulders_y

    if is_correct:
        if pose_check_time is None:
            pose_check_time = current_time
        elif current_time - pose_check_time > 1.0:
            if current_time - last_sound_time > SOUND_COOLDOWN:
                if success_sound:
                    success_sound.play()
                    last_sound_time = current_time
                pose_check_time = None
    else:
        pose_check_time = None

    return is_correct


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Помилка: не вдалося отримати кадр з камери!")
        break

    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (1280, 960))

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(rgb_frame)

    # Відображення інтерфейсу
    if overlay_image is not None:
        oh, ow = overlay_image.shape[:2]
        x_offset = frame.shape[1] - ow
        frame[0:oh, x_offset:x_offset + ow] = overlay_image

    if result.pose_landmarks:
        h, w, _ = frame.shape
        landmarks = result.pose_landmarks.landmark

        # Відображення скелета
        if show_skeleton:
            mp_drawing.draw_landmarks(
                frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)
            )

        # Перевірка пози
        check_current_pose(landmarks, pose_index, h, w)

        # Обробка кнопок
        current_time = time.time()
        for button_name in buttons:
            button_pressed = False
            for lm_part in [mp_pose.PoseLandmark.RIGHT_INDEX, mp_pose.PoseLandmark.LEFT_INDEX]:
                lm = landmarks[lm_part]
                if lm.visibility < 0.5:
                    continue
                x, y = int(lm.x * w), int(lm.y * h)
                if check_button_press(x, y, button_name):
                    if button_press_time[button_name] is None:
                        button_press_time[button_name] = current_time
                    elif current_time - button_press_time[button_name] > 1:
                        if button_name == "Вихід":
                            show_goodbye_and_exit(frame)
                        elif button_name == "Скелет":
                            show_skeleton = not show_skeleton
                        elif button_name == "Наступна поза":
                            pose_index = (pose_index + 1) % len(poses)
                            overlay_image = load_pose_image(pose_index)
                        elif button_name == "Попередня поза":
                            pose_index = (pose_index - 1) % len(poses)
                            overlay_image = load_pose_image(pose_index)
                        button_press_time[button_name] = None
                    button_pressed = True
                    break
            if not button_pressed:
                button_press_time[button_name] = None

    # Конвертація для PIL
    frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(frame_pil)

    for button_name, (bx, by) in buttons.items():
        color = (0, 0, 200) if button_press_time[button_name] is None else (0, 200, 0)
        # Малювання прямокутника
        draw.rectangle([bx, by, bx + BUTTON_WIDTH, by + BUTTON_HEIGHT], fill=color)
        # Малювання тексту
        if font:
            text_bbox = draw.textbbox((0, 0), button_name, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            text_x = bx + (BUTTON_WIDTH - text_width) / 2
            text_y = by + (BUTTON_HEIGHT - text_height) / 2
            draw.text((text_x, text_y), button_name, font=font, fill=(255, 255, 255))

    # Конвертація назад до OpenCV
    frame = cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)

    cv2.imshow('Mediapipe Yoga', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
show_goodbye_and_exit(frame)
