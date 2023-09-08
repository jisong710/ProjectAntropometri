import cv2

class pose_estimation:
# Mulai webcam
    def __init__():
        cap = cv2.VideoCapture(0)
        # Load pre-trained cascade classifier
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

        while True:
            # Baca frame dari webcam
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Deteksi wajah
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                
                # Deteksi mata dalam wajah yang terdeteksi
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

            # Tampilkan frame dengan deteksi wajah dan mata
            cv2.imshow('Deteksi Wajah dan Mata', frame)

            # Tekan tombol 'q' untuk keluar dari loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Bebaskan sumber daya dan tutup jendela
        cap.release()
        cv2.destroyAllWindows()
