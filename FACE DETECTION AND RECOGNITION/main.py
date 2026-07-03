import cv2
import face_recognition
import os

# Load Haar Cascade
import cv2

cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

known_faces = []
known_names = []

# Load known faces
dataset_path = "dataset"

for file in os.listdir(dataset_path):
    image = face_recognition.load_image_file(os.path.join(dataset_path, file))
    encodings = face_recognition.face_encodings(image)

    if len(encodings) > 0:
        known_faces.append(encodings[0])
        known_names.append(os.path.splitext(file)[0])

# Open Webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    encodings = face_recognition.face_encodings(rgb)

    for ((x, y, w, h), face_encoding) in zip(faces, encodings):

        matches = face_recognition.compare_faces(
            known_faces,
            face_encoding
        )

        name = "Unknown"

        if True in matches:
            index = matches.index(True)
            name = known_names[index]

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

        cv2.putText(
            frame,
            name,
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,0),
            2
        )

    cv2.imshow("Face Detection & Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()