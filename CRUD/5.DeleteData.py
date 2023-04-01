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

#To delete the data
# db.child("pyrebaserealtimedbdemo").child("todolistA").child("monday").child("paper").remove()
# db.child("pyrebaserealtimedbdemo").child("todolistA").child("wednesday").child("project").child("deadline").remove()

#to delete the data by auto generated key
monday_tasks = db.child("pyrebaserealtimedbdemo").child("todolistB").child("monday").get()

for task in monday_tasks.each():
    """print(task.val())
    print(task.key())"""

    if task.val()['name'] == "paper":
        # print(task.val())
        # print(task.key())
        key = task.key()

db.child("pyrebaserealtimedbdemo").child("todolistB").child("monday").child(key).child("deadline").remove()
