import cv2
import os
import pickle 
import face_recognition
import numpy as np
import cvzone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    "databaseURL":"https://face-recognition-system-b41c1-default-rtdb.firebaseio.com/"
})

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


modeType=0


imgBackground = cv2.imread('resources/backgroundImg.png')


#importing modes images 
folderModePath="resources/modes"
modePathList = os.listdir(folderModePath)
modePathList.sort()

imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))
  


# load the encodings 
print("Loading Encoding files...")
file = open('Encodefile.p','rb')
encodeListKnownsWithId = pickle.load(file)
file.close()
encodeListKnown,studentIds = encodeListKnownsWithId
# print(studentIds)
print("Encoding files Loaded")

counter = 0 

id=-1
while True:
    success, img = cap.read()
    
    #  Resize the webcam image to fit the blue box
    target_w, target_h = 332, 250
    img_resized_for_display = cv2.resize(img, (target_w, target_h))
    
    #  Put the image on the background immediately
    # This ensures the image is the bottom layer
    bg_x, bg_y = 36, 93 
    imgBackground[bg_y:bg_y + target_h, bg_x:bg_x + target_w] = img_resized_for_display

    #  Perform Face Detection
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)
    
    
    if faceCurFrame:
        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            
            matchIndex = np.argmin(faceDis)
            
            if matches[matchIndex]:
                # Get original coordinates
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                
                #  Scale and Offset Coordinates
                # Scale Factor: New Size / Original Camera Size
                scale_x = target_w / 640
                scale_y = target_h / 480
                
                # Apply scale + Add the offset (bg_x, bg_y) to move it to the blue box position
                x_new = int(x1 * scale_x) + bg_x
                y_new = int(y1 * scale_y) + bg_y
                w_new = int((x2 - x1) * scale_x)
                h_new = int((y2 - y1) * scale_y)
                
                bbox = (x_new, y_new, w_new, h_new)

                #  DRAW SECOND: Draw the box on top of the already pasted image
                # added t=3 to make the thickness visible
                imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0, t=2, colorR=(0, 255, 0))  
                
                id = studentIds[matchIndex]
                
                if counter == 0:
                
                    counter = 1
                    modeType = 1# Keep it 1(Scanning) initially
                    
    
        
        if counter != 0:
            if counter ==1:
                studentInfo = db.reference(f'Students/{id}').get()
                # print(studentInfo['total_attendence'])
                #  Get the student Image from local storage
                
                imgStudent = cv2.imread(f'images/{id}.png')
                
                # Resize the student image to fit the square on the card
                
                imgStudent = cv2.resize(imgStudent, (121, 121))
                
                # Updating the data on server 
                
                datetimeObject = datetime.strptime(studentInfo['last_attendance_time'],
                                                    "%Y-%m-%d %H:%M:%S")
                secondElapsed = (datetime.now()-datetimeObject).total_seconds()
                
                if secondElapsed>5:
                    ref = db.reference(f'Students/{id}')
                    studentInfo['total_attendence']+=1
                    ref.child('total_attendence').set(studentInfo['total_attendence'])
                    ref.child('last_attendance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                else:
                    modeType = 3
                    counter=0
                    imgRight = imgModeList[modeType]
                    imgRight = cv2.resize(imgRight, (230, 350))
                    imgBackground[25:25+350, 432:432+230] = imgRight 
            
            if modeType != 3 :
                    
                if 10<counter<50:
                    modeType=2   
                    
                    
                # Rightside image handling
                if counter < 10:
            
                
                    
                    imgRight = imgModeList[modeType]
                    imgRight = cv2.resize(imgRight, (230, 350))
                    imgBackground[25:25+350, 432:432+230] = imgRight 
                    
                    #adding student image on card
                    imgBackground[99:99+121, 488:488+121] = imgStudent
                    
                    
                    cv2.putText(imgBackground, str(studentInfo['total_attendence']), (468, 65),
                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1,cv2.LINE_AA)
                    
                    
                    
                    # ID (White text on Purple pill)
                    # Adjust (545, 274) if it's not perfectly inside the pill
                    cv2.putText(imgBackground, f"{id}", (545, 274),
                                cv2.FONT_HERSHEY_COMPLEX, 0.4, (0,0,0), 1, cv2.LINE_AA)
                    # print(id)
                    
                    #Major (White text on Purple pill)
                    # Adjust (545, 306) if needed
                    cv2.putText(imgBackground, str(studentInfo['major']), (545, 306),
                                cv2.FONT_HERSHEY_COMPLEX, 0.4, (0,0,0), 1, cv2.LINE_AA)
                    
                    (w, h), _ = cv2.getTextSize(studentInfo['name'], cv2.FONT_HERSHEY_COMPLEX, 0.5, 1)
                    
                    # 432 is where the card starts. 230 is the width. 
                    # The center of the card is 432 + (230/2) = 547
                    # We subtract half the text width (w/2) to center it.
                    offset = (432 + 115) - (w // 2)
                    
                    cv2.putText(imgBackground, str(studentInfo['name']), (offset, 238),
                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (50, 50, 50), 1, cv2.LINE_AA)
                    
                    # 1. Standing (Left Icon) - 'G' or 'B' etc.
                    cv2.putText(imgBackground, str(studentInfo['standing']), (490, 345),
                                cv2.FONT_HERSHEY_COMPLEX, 0.4, (50, 50, 50), 1, cv2.LINE_AA)

                    # 2. Starting Year (Middle Icon)
                    cv2.putText(imgBackground, str(studentInfo['year']), (550, 345),
                                cv2.FONT_HERSHEY_COMPLEX, 0.4, (50, 50, 50), 1, cv2.LINE_AA)

                    # 3. Current Year (Right Icon)
                    cv2.putText(imgBackground, str(studentInfo['starting_year']), (610, 345),
                                cv2.FONT_HERSHEY_COMPLEX, 0.4, (50, 50, 50), 1, cv2.LINE_AA)
                
                
                if 50<counter<60:
                    modeType = 3
                    imgRight = imgModeList[modeType]
                    imgRight = cv2.resize(imgRight, (230, 350))
                    imgBackground[25:25+350, 432:432+230] = imgRight 
                counter+=1
                if counter > 60:
                    counter = 0
                    modeType = 1
                    studentInfo = []
                    imgStudent = []
                    imgRight = imgModeList[modeType]
                    imgRight = cv2.resize(imgRight, (230, 350))
                    imgBackground[25:25+350, 432:432+230] = imgRight
        else:
            # Show the empty card if no face is detected
            imgRight = imgModeList[modeType]
            imgRight = cv2.resize(imgRight, (230, 350))
            imgBackground[25:25+350, 432:432+230] = imgRight
    else:
        modeType=0
        counter=0
        imgRight = imgModeList[modeType]
        imgRight = cv2.resize(imgRight, (230, 350))
        imgBackground[25:25+350, 432:432+230] = imgRight 
        
    cv2.imshow("face recognition", imgBackground)
    cv2.waitKey(1)