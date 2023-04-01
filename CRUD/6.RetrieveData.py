import pyrebase 

firebaseConfig = {
    "apiKey": "AIzaSyDSLcLu6GSxece0XVRLZKIvwQk9qx1t4BU",
    "authDomain": "authdemo-91b1a.firebaseapp.com",
    "projectId": "authdemo-91b1a",
    "databaseURL": "https://authdemo-91b1a-default-rtdb.firebaseio.com",
    "storageBucket": "authdemo-91b1a.appspot.com",
    "messagingSenderId": "769208992989",
    "appId": "1:769208992989:web:7e40535e9201a0c00f4734",
    "measurementId": "G-56WFZTBLVL"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

"""
data1 = {"address": "Los Angeles", "age": 20, "firstname": "Jane", "lastname": "Doe"}
data2 = {"address": "New York", "age": 30, "firstname": "John", "lastname": "Smith"}
data3 = {"age": 32, "firstname": "Marc", "lastname": "Johnson"}
data4 = {"address": "New York", "age": 44, "firstname": "Eric", "lastname": "Brown"}

db.child("RetrieveData").child("users").push(data1)
db.child("RetrieveData").child("users").push(data2)
db.child("RetrieveData").child("users").push(data3)
db.child("RetrieveData").child("users").push(data4)
"""

