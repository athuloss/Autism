
import cv2
import mediapipe as mp
import numpy as np
import platform
import time
import threading


stop_flag = False
thread = None

def beep():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 200)
    else:
        print('\a')

def get_gaze_ratio(landmarks, eye_indices, gray, frame_width, frame_height):
    points = []
    for idx in eye_indices:
        x = int(landmarks[idx].x * frame_width)
        y = int(landmarks[idx].y * frame_height)
        points.append((x, y))
    points = np.array(points, np.int32)
    
    mask = np.zeros_like(gray)
    cv2.fillPoly(mask, [points], 255)
    eye = cv2.bitwise_and(gray, gray, mask=mask)
    
    min_x = np.min(points[:, 0])
    max_x = np.max(points[:, 0])
    min_y = np.min(points[:, 1])
    max_y = np.max(points[:, 1])
    
    gray_eye = eye[min_y:max_y, min_x:max_x]
    if gray_eye.size == 0:
        return 1.0
    _, threshold_eye = cv2.threshold(gray_eye, 70, 255, cv2.THRESH_BINARY)
    height, width = threshold_eye.shape
    left_half = threshold_eye[:, :width // 2]
    right_half = threshold_eye[:, width // 2:]
    
    left_white = cv2.countNonZero(left_half)
    right_white = cv2.countNonZero(right_half)
    if left_white + right_white == 0:
        return 1.0
    return left_white / (left_white + right_white)

def gaze_detection_loop():
    global stop_flag
    
    calibrated_center = 0.51
    deviation_threshold = 0.1
    left_eye_indices = [33, 7, 163, 144, 145, 153, 154, 155, 133]
    right_eye_indices = [263, 249, 390, 373, 374, 380, 381, 382, 362]

    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(
        static_image_mode=False,
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )
    cap = cv2.VideoCapture(0)
    away_start_time = None
    alerted = False

    while not stop_flag:
        ret, frame = cap.read()
        if not ret:
            break

        frame_height, frame_width = frame.shape[:2]
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                left_gaze = get_gaze_ratio(face_landmarks.landmark, left_eye_indices, gray, frame_width, frame_height)
                right_gaze = get_gaze_ratio(face_landmarks.landmark, right_eye_indices, gray, frame_width, frame_height)
                current_gaze = (left_gaze + right_gaze) / 2

                
                if abs(current_gaze - calibrated_center) > deviation_threshold:
                    if away_start_time is None:
                        away_start_time = time.time()
                        alerted = False
                    else:
                        if not alerted and (time.time() - away_start_time >= 5):
                            beep()
                            alerted = True
                else:
                    away_start_time = None
                    alerted = False

        cv2.imshow("Gaze Detection", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    face_mesh.close()

import cv2
import mediapipe as mp
import numpy as np
import platform
import time
import threading


stop_flag = False
thread = None


if platform.system() == "Windows":
    import winsound
    def beep():
        winsound.Beep(1000, 200)
else:
    def beep():
        print('\a')


mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

def get_gaze_ratio(landmarks, eye_indices, gray, frame_width, frame_height):
    points = []
    for idx in eye_indices:
        x = int(landmarks[idx].x * frame_width)
        y = int(landmarks[idx].y * frame_height)
        points.append((x, y))
    points = np.array(points, np.int32)
    
    mask = np.zeros_like(gray)
    cv2.fillPoly(mask, [points], 255)
    eye = cv2.bitwise_and(gray, gray, mask=mask)
    
    min_x = np.min(points[:, 0])
    max_x = np.max(points[:, 0])
    min_y = np.min(points[:, 1])
    max_y = np.max(points[:, 1])
    
    gray_eye = eye[min_y:max_y, min_x:max_x]
    if gray_eye.size == 0:
        return 1.0  
    
    _, threshold_eye = cv2.threshold(gray_eye, 70, 255, cv2.THRESH_BINARY)
    height, width = threshold_eye.shape
    left_half = threshold_eye[:, :width // 2]
    right_half = threshold_eye[:, width // 2:]
    
    left_white = cv2.countNonZero(left_half)
    right_white = cv2.countNonZero(right_half)
    
    if left_white + right_white == 0:
        return 1.0
    else:
        return left_white / (left_white + right_white)

def gaze_detection_loop():
    
    global stop_flag
    calibrated_center = 0.51
    deviation_threshold = 0.1

    left_eye_indices = [33, 7, 163, 144, 145, 153, 154, 155, 133]
    right_eye_indices = [263, 249, 390, 373, 374, 380, 381, 382, 362]

    cap = cv2.VideoCapture(0)
    away_start_time = None
    alerted = False

    while not stop_flag:
        ret, frame = cap.read()
        if not ret:
            break

        frame_height, frame_width = frame.shape[:2]
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        display_text = ""
        current_gaze = None

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                left_gaze = get_gaze_ratio(face_landmarks.landmark, left_eye_indices, gray, frame_width, frame_height)
                right_gaze = get_gaze_ratio(face_landmarks.landmark, right_eye_indices, gray, frame_width, frame_height)
                current_gaze = (left_gaze + right_gaze) / 2

               
                for idx in left_eye_indices + right_eye_indices:
                    x = int(face_landmarks.landmark[idx].x * frame_width)
                    y = int(face_landmarks.landmark[idx].y * frame_height)
                    cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

                
                if abs(current_gaze - calibrated_center) > deviation_threshold:
                    display_text = "Staring Away"
                    if away_start_time is None:
                        away_start_time = time.time()
                        alerted = False
                    else:
                        if not alerted and (time.time() - away_start_time >= 5):
                            beep()
                            alerted = True
                else:
                    display_text = "Looking at Screen"
                    away_start_time = None
                    alerted = False
        else:
            display_text = "No Face Detected"
            away_start_time = None
            alerted = False

        cv2.putText(frame, display_text, (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 0, 255) if display_text == "Staring Away" else (0, 255, 0), 2)
        
        if current_gaze is not None:
            cv2.putText(frame, f"Gaze: {current_gaze:.2f}", (50, 90),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.putText(frame, f"Center: {calibrated_center:.2f}", (50, 130),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

        cv2.imshow("Gaze Detection", frame)
        if cv2.waitKey(1) & 0xFF == 27:  
            break

    cap.release()
    cv2.destroyAllWindows()

def start_gaze_detection():
   
    global stop_flag, thread
    if thread is None or not thread.is_alive():
        stop_flag = False
        thread = threading.Thread(target=gaze_detection_loop)
        thread.start()

def stop_gaze_detection():
    
    global stop_flag, thread
    stop_flag = True
    if thread is not None:
        thread.join()
        thread = None

if __name__ == "__main__":
    start_gaze_detection()

