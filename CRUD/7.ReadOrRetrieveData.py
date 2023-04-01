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

#Before running this code we have to add new rule into firebase 
"""Ex:-
"users": {
    	".indexOn": ["age", "address", "firstname", "lastname"]
    },
"""
#it means we are telling firebase that we want to perform complex queries on these indexes or columns.

#For getting conditional data
# result = db.child("RetrieveData").child("users").order_by_child("firstname").equal_to("Jane").get()

#for getting top 5 ones whose age is 44. Try it by doing 1 instead of 5.
# result = db.child("RetrieveData").child("users").order_by_child("age").equal_to(44).limit_to_first(5).get()

#To filter the users age -> start_at(30) means age greater than or equal to 30.
result = db.child("RetrieveData").child("users").order_by_child("age").start_at(30).get()

#less than or equal to.
result = db.child("RetrieveData").child("users").order_by_child("age").end_at(44).get()

#To get all of them
result = db.child("RetrieveData").child("users").order_by_key().get()

#To get some of them
result = db.child("RetrieveData").child("users").order_by_key().limit_to_first(3).get()
print(result.val())