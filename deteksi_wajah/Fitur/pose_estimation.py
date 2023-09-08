import cv2
import mediapipe as mp

class pose_estimation:
    def __init__(self):
        self.mp_face_detection = mp.solutions.face_detection
        self.face_detection = self.mp_face_detection.FaceDetection()
        self.cap = cv2.VideoCapture(0)

    def detect_face(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.face_detection.process(rgb_frame)

            if results.detections:
                for detection in results.detections:
                    bboxC = detection.location_data.relative_bounding_box
                    ih, iw, _ = frame.shape
                    x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                    face_roi = frame[y:y+h, x:x+w]
                    cv2.imshow('Face Detection', face_roi)
            cv2.imshow('Full', frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
            elif key == 32:
                # Pause on space bar
                cv2.waitKey(0)

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    face_detector = pose_estimation()
    face_detector.detect_face()

