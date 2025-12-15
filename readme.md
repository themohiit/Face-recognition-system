# 📸 Face Recognition Attendance System

A real-time, smart attendance system built with Python, OpenCV, and Firebase. This application detects faces using a webcam, verifies them against a known database of encodings, and updates attendance records in a Firebase Realtime Database instantly.

## 🚀 Features

* **Real-time Face Detection**: Uses the `face_recognition` library to detect and identify students instantly.
* **Live Database Integration**: Fetches student details (Name, Major, Year, Attendance Count) from **Firebase Realtime Database**.
* **Smart Attendance Logic**:
    * Prevents duplicate attendance entries (30-second cooldown timer).
    * Updates "Last Attendance Time" and increments total attendance count automatically.
* **Dynamic UI**:
    * Custom graphical interface using OpenCV and cvzone.
    * Displays student profile pictures from local storage.
    * Smooth mode transitions (Scanning → Loading → Student Details → Marked).
* **Anti-Spoofing/Optimization**: Includes resizing and scaling logic to ensure performance on standard hardware.

## 🛠️ Tech Stack

* **Language**: Python 3.x
* **Computer Vision**: OpenCV (`cv2`), cvzone
* **Face Recognition**: `face_recognition`, `dlib`
* **Database**: Firebase Admin SDK (Realtime Database)
* **Data Handling**: NumPy, Pickle

## 📂 Project Structure

```text
face_recognition_system/
│
├── images/                 # Student profile photos (filename = StudentID.png)
├── resources/              # UI Assets
│   ├── backgroundImg.png   # Main background interface
│   └── modes/              # Status cards (Scanning, Details, Marked)
│
├── app.py                  # Main application script
├── addDataToDatabase.py    # Script to upload student info to Firebase
├── Encodefile.p            # Generated file storing face encodings
├── serviceAccountKey.json  # Firebase Secret Key (NOT INCLUDED)
└── requirements.txt        # Dependencies
