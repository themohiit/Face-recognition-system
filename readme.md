
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

⚙️ Setup & Installation
 * Clone the repo : https://github.com/themohiit/Face-recognition-system


 * Install Dependencies
   It is recommended to use a virtual environment
   run: pip install opencv-python numpy face_recognition firebase-admin cvzone
 * Firebase Setup
   * Go to Firebase Console.
   * Create a new project and set up Realtime Database.
   * Go to Project Settings > Service Accounts.
   * Generate a New Private Key.
   * Download the JSON file, rename it to serviceAccountKey.json, and place it in the project root folder.
   * Note: Do NOT share this file or upload it to GitHub.
 * Add Student Images
   * Place student images in the images/ folder.
   * Rename them to match the Student ID (e.g., 34216.png).
🏃‍♂️ How to Run
Step 1: Upload Data to Database
First, edit addDataToDatabase.py with your student details and run it once to populate Firebase.
python addDataToDatabase.py

Step 2: Generate Encodings
Ensure you have run your encoding generator script (if separate) or that Encodefile.p is present in the directory.
Step 3: Start the System
Run the main application:
python app.py

⚠️ Important Notes
 * Webcam: Ensure your webcam is connected and accessible (ID 0 or 1 in cv2.VideoCapture).
 * Internet: The app requires an active internet connection to communicate with Firebase.
 * Graphics: Ensure the resources/ folder contains the correct PNG assets (backgroundImg.png and modes/ folder) for the UI to load correctly.
🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.
📜 License
This project is open-source and available under the MIT License.

