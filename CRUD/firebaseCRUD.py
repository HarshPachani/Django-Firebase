import pyrebase

config = {
    "apiKey": "AIzaSyDRbVkM0bFv6TSvUri32xVqwjx5R4gHWGg",
    "authDomain": "fir-project-cc581.firebaseapp.com",
    "projectId": "fir-project-cc581",
    "databaseURL": "https://fir-project-cc581-default-rtdb.firebaseio.com",
    "storageBucket": "fir-project-cc581.appspot.com",
    "messagingSenderId": "524463407939",
    "appId": "1:524463407939:web:23f32e1330311864a1e5f6",
    "measurementId": "G-WXZFNFZVQB"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

data = {"Age": 21, "name": "Harsh", "Likes Pizza": True}

#CRUD Operations Starts
#Create Data

