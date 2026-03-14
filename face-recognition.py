import os
import cv2
import face_recognition
import pandas as pd
from datetime import datetime

known_images_folder = r'C:\Users\VSE\Desktop\AI\attendance\dataset\Anshika'  

known_encodings = []
known_files = [] 

for filename in os.listdir(known_images_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):  
        path = os.path.join(known_images_folder, filename)
        known_image = face_recognition.load_image_file(path)
        encodings = face_recognition.face_encodings(known_image)
        if encodings:  
            known_encodings.append(encodings[0])
            known_files.append(filename)  
            print(f"Encoded {filename}")
        else:
            print(f"No faces found in {filename}")

video_capture = cv2.VideoCapture(0)

attendance_list = []

if not video_capture.isOpened():
    print("Error: Could not open video stream.")
else:
    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to grab frame.")
            break

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        print(f"Detected {len(face_locations)} faces")

        for face_location, face_encoding in zip(face_locations, face_encodings):
            results = face_recognition.compare_faces(known_encodings, face_encoding)
            match = "Unknown"

            face_distances = face_recognition.face_distance(known_encodings, face_encoding)
            best_match_index = face_distances.argmin()

            if results[best_match_index]:
                match = known_files[best_match_index]  
            if match != "Unknown":
                attendance_list.append({"Name": match, "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

            top, right, bottom, left = [v * 4 for v in face_location]  
            color = (0, 255, 0) if match != "Unknown" else (0, 0, 255)
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.putText(frame, match, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, 2)


        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()

cv2.destroyAllWindows()

if attendance_list:
    df = pd.DataFrame(attendance_list)
    df.to_excel('attendance.xlsx', index=False)
    print("Attendance has been saved to attendance.xlsx")
else:
    print("No attendance records to save.")
 
