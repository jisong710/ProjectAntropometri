import cv2

class pose_estimation:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        self.cap = cv2.VideoCapture(0)

    def detect_and_display_eyes(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

            for (x, y, w, h) in faces:
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                eyes = self.eye_cascade.detectMultiScale(roi_gray)
                
                if len(eyes) == 2:
                    left_eye = eyes[0]
                    right_eye = eyes[1]
                    
                    if(right_eye[1]-left_eye[1]+left_eye[3] > 0 and right_eye[0]-left_eye[0]+left_eye[2] > 0):
                        eye_roi = roi_color[left_eye[1]:right_eye[1]+right_eye[3], left_eye[0]:right_eye[0]+right_eye[2]]
                    elif(left_eye[1]-right_eye[1]+right_eye[3] > 0 and left_eye[0]-right_eye[0]+right_eye[2] > 0):
                        eye_roi = roi_color[right_eye[1]:left_eye[1]+left_eye[3], right_eye[0]:left_eye[0]+left_eye[2]] 
                    if(eye_roi.size >0):                
                        cv2.imshow('Eye', eye_roi)
            cv2.imshow('face', frame)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break
            elif key == 32:
                # Pause on space bar
                cv2.waitKey(0)

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    eye_detector = pose_estimation()
    eye_detector.detect_and_display_eyes()

