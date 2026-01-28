import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    "databaseURL":"https://face-recognition-system-b41c1-default-rtdb.firebaseio.com/"
})
ref = db.reference('Students')

data = {
    "34216" :
        {"name" : "Elon Musk",
         "major":"Robotics & AI",
         "starting_year":2022,
         "total_attendence":3,
         "standing":"X",
         "year":4,
         "last_attendance_time":"2025-12-14 09:04:54"
         },
    "54812" :
        {"name" : "Mohit Singh",
         "major":"CS & AI",
         "starting_year":2023,
         "total_attendence":5,
         "standing":"G",
         "year":3,
         "last_attendance_time":"2025-12-14 09:04:54"
         },
    "89786" :
        {"name" : "Khushi Sharma ",
         "major":"Non med",
         "starting_year":2023,
         "total_attendence":5,
         "standing":"G",
         "year":3,
         "last_attendance_time":"2025-12-14 09:04:54"
         },
    "12345" :
        {"name" : "Sanju",
         "major":"BCOM",
         "starting_year":2023,
         "total_attendence":5,
         "standing":"G",
         "year":3,
         "last_attendance_time":"2025-12-14 09:04:54"
         },
    "54321" :
        {"name" : "kaku",
         "major":"non-med",
         "starting_year":2024,
         "total_attendence":5,
         "standing":"G",
         "year":1,
         "last_attendance_time":"2025-12-14 09:04:54"
         },
    "56432" :
        {"name" : "pui",
         "major":"Bcom",
         "starting_year":2023,
         "total_attendence":5,
         "standing":"G",
         "year":3,
         "last_attendance_time":"2025-12-14 09:04:54"
         },
    "90876" :
        {"name" : "shiku",
         "major":"Teaching",
         "starting_year":2021,
         "total_attendence":5,
         "standing":"G",
         "year":3,
         "last_attendance_time":"2025-12-14 09:04:54"
         },
    "10876" :
        {"name" : "Renu devi",
         "major":"Ml",
         "starting_year":2021,
         "total_attendence":5,
         "standing":"G",
         "year":3,
         "last_attendance_time":"2025-12-14 09:04:54"
         },
    "43217" :
        {"name" : "Kartik",
         "major":"none",
         "starting_year":2021,
         "total_attendence":5,
         "standing":"G",
         "year":0,
         "last_attendance_time":"2025-12-14 09:04:54"
         },
    "65456" :
        {"name" : "Pinki",
         "major":"Ai",
         "starting_year":2021,
         "total_attendence":5,
         "standing":"G",
         "year":3,
         "last_attendance_time":"2025-12-14 09:04:54"
         },
}

for key,value in data.items():
    ref.child(key).set(value)
