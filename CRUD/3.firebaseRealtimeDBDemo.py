# import pyrebase

# firebaseConfig = {
#     "apiKey": "AIzaSyDSLcLu6GSxece0XVRLZKIvwQk9qx1t4BU",
#     "authDomain": "authdemo-91b1a.firebaseapp.com",
#     "projectId": "authdemo-91b1a",
#     "databaseURL": "https://authdemo-91b1a-default-rtdb.firebaseio.com",
#     "storageBucket": "authdemo-91b1a.appspot.com",
#     "messagingSenderId": "769208992989",
#     "appId": "1:769208992989:web:7e40535e9201a0c00f4734",
#     "measurementId": "G-56WFZTBLVL"
# }

# firebase = pyrebase.initialize_app(firebaseConfig)

# db = firebase.database()

# #push data
# data = {
#     "Name": "Harsh", "Age": 20, "Address": ["Ahmedabad", "Junagadh", "Gandhinagar"]
# }

# db.Push(data)

import pyrebase

#Initialize Firebase
firebaseConfig={"apiKey": "AIzaSyDm2HeGl3bApix5KsbhI8NOjdwXkhNTaJM",
    "authDomain": "trialauth-7eea1.firebaseapp.com",
    "databaseURL": "https://trialauth-7eea1.firebaseio.com",
    "projectId": "trialauth-7eea1",
    "storageBucket": "trialauth-7eea1.appspot.com",
    "messagingSenderId": "441088628124",
    "appId": "1:441088628124:web:6fc6142f0e28275e2f2459",
    "measurementId": "G-NKL8XN36NX"}

firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()

#Push Data
data={"age":20, "address":["new york", "los angeles"]}
print(db.push(data)) #unique key is generated