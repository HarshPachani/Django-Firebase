import pyrebase 

firebaseConfig = {
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
db = firebase.database()

users = db.get()
print(users)

for user in users.each():
    print(user[0].val(), "\n")