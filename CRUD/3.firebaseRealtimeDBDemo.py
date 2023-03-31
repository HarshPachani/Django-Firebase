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

#push data
data = {
    "Name": "Harsh", "Age": 20, "Address": ["Ahmedabad", "Junagadh", "Gandhinagar"]
}
# print(db.push(data)) #unique key is generated
db.child("Branch").child("Employee").child("Male employee").push(data)

#Create Your own key with set() method.
# data = {
#     "Age": 20, "Address": "[Gujarat]"
# }
# db.child("Harsh").set(data)