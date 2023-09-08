import tkinter as tk
from tkinter import ttk
import threading
import math
import cv2
import numpy as np
from sklearn.linear_model import LinearRegression
from PIL import Image, ImageTk
import pandas as pd
import mediapipe as mp
from openvino.inference_engine import IECore

# Inisialisasi Linear Regression model
model = LinearRegression()

# Inisialisasi OpenVINO
ie = IECore()
net = ie.read_network(model='models/pose_landmark_heavy_FP32.xml', weights='models/pose_landmark_heavy_FP32.bin')
exec_net = ie.load_network(network=net, device_name="CPU")

# Fungsi untuk mendeteksi pose dan memperbarui GUI
def detect_pose():
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
    
    while True:
        ret, frame = cap.read()

        results = pose.process(frame)
        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            left_shoulder_landmark = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
            right_shoulder_landmark = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]

            center_landmark_x = (int(left_shoulder_landmark.x) + int(right_shoulder_landmark.x)) / 2
            center_landmark_y = (int(left_shoulder_landmark.y) + int(right_shoulder_landmark.y)) / 2

            left_shoulder_tilt = math.degrees(math.atan2(center_landmark_y - left_shoulder_landmark.y,
                                                         center_landmark_x - left_shoulder_landmark.x))
            right_shoulder_tilt = math.degrees(math.atan2(center_landmark_y - right_shoulder_landmark.y,
                                                          center_landmark_x - right_shoulder_landmark.x))

            shoulder_tilt = (left_shoulder_tilt, right_shoulder_tilt)
            average_tilt = np.diff(shoulder_tilt)

            result_label.config(text=f"Left Shoulder Tilt: {left_shoulder_tilt:.2f} degrees\n"
                                     f"Right Shoulder Tilt: {right_shoulder_tilt:.2f} degrees")

            new_data = pd.DataFrame([[left_shoulder_tilt, right_shoulder_tilt]], columns=['Left_Shoulder', 'Right_Shoulder'])
            new_label = pd.Series([average_tilt], name='Average_Tilt')

            # Gunakan threading untuk menjalankan proses pembelajaran dan prediksi secara terpisah
            threading.Thread(target=incremental_learning, args=(new_data, new_label)).start()
            threading.Thread(target=predict_and_display, args=(new_data,)).start()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=img)
        video_label.config(image=img)
        video_label.image = img

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Fungsi untuk melakukan pembelajaran incrementally
def incremental_learning(new_data, new_labels):
    global X_train, y_train
    X_train = pd.concat([X_train, new_data], ignore_index=True)
    y_train = pd.concat([y_train, new_labels], ignore_index=True)
    model.fit(X_train, y_train)

# Fungsi untuk melakukan prediksi dan menampilkan hasil
def predict_and_display(new_data):
    predicted_tilt = model.predict(new_data)
    predicted_label.config(text=f"Predicted Tilt: {predicted_tilt[0]:.2f} degrees")

# Membaca dataset dari file CSV
dataset_path = 'dataset.csv'
dataset = pd.read_csv(dataset_path)

# Pisahkan fitur (X) dan target (y) dari dataset
X_train = dataset[['Left_Shoulder', 'Right_Shoulder']]
y_train = dataset['Average_Tilt']

# Membuat GUI menggunakan Tkinter
root = tk.Tk()
root.title("Shoulder Tilt Detection with Incremental Linear Regression, Blazepose, and Mediapipe")

# Buat frame utama dengan tampilan Material Design
style = ttk.Style()
style.theme_use("alt")
main_frame = ttk.Frame(root)
main_frame.pack(padx=20, pady=20)

# Tombol untuk memulai deteksi
detect_button = ttk.Button(main_frame, text="Detect Shoulder Tilt", command=detect_pose)
detect_button.pack()

# Label untuk menampilkan hasil deteksi
result_label = ttk.Label(main_frame, text="")
result_label.pack()

# Label untuk menampilkan prediksi kemiringan bahu
predicted_label = ttk.Label(main_frame, text="")
predicted_label.pack()

# Frame untuk menampilkan video
video_frame = ttk.Frame(main_frame)
video_frame.pack()

video_label = ttk.Label(video_frame)
video_label.pack()

# Inisialisasi webcam
cap = cv2.VideoCapture(0)  # 0 untuk webcam internal, ganti dengan angka sesuai perangkat Anda

# Membuat thread untuk deteksi pose
pose_thread = threading.Thread(target=detect_pose)
pose_thread.start()

# Mulai GUI loop
root.mainloop()
