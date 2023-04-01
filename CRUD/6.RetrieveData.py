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

firebaseConfig2 = {
    "apiKey": "AIzaSyCzneUDuxGW36MViwUQf2gnT0w7XIyzi1c",
    "authDomain": "login-8a1a8.firebaseapp.com",
    "databaseURL": "https://login-8a1a8-default-rtdb.firebaseio.com",
    "projectId": "login-8a1a8",
    "storageBucket": "login-8a1a8.appspot.com",
    "messagingSenderId": "414258770200",
    "appId": "1:414258770200:web:4faf9a519d3cc54cf42e6d",
    "measurementId": "G-H2GCMN40BS"
}

firebase = pyrebase.initialize_app(firebaseConfig)
firebase2 = pyrebase.initialize_app(firebaseConfig2)

db = firebase.database()
db2 = firebase2.database()


"""
#Created data.

data1 = {"address": "Los Angeles", "age": 20, "firstname": "Jane", "lastname": "Doe"}
data2 = {"address": "New York", "age": 30, "firstname": "John", "lastname": "Smith"}
data3 = {"age": 32, "firstname": "Marc", "lastname": "Johnson"}
data4 = {"address": "New York", "age": 44, "firstname": "Eric", "lastname": "Brown"}

db.child("RetrieveData").child("users").push(data1)
db.child("RetrieveData").child("users").push(data2)
db.child("RetrieveData").child("users").push(data3)
db.child("RetrieveData").child("users").push(data4)
"""

#Retrieve Data
users = db.child("RetrieveData").child("users").get()
# print(users.val())

# users2 = db2.get()
# print(users2.val())

#Iterate over keys
print("\n\t\t\tIterate Over the keys")
for user in users.each():
    print("key: ", user.val())
    print("Values: ", user.val())
    print()

#You can also use shallow method to get keys.
users = db.child("RetrieveData").child("users").shallow().get()
print("\n\t\t\t\tUsing Shallow() method\n", users.val())