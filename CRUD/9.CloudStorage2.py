import pyrebase
import urllib #It is a standard way to read file from the internet.

firebaseConfig = {
    "apiKey": "AIzaSyDmmJcWxCFnAzgBdDcNTJSCRlWvGIU6414",
    "authDomain": "realtimedbstoragedemo-2c0fb.firebaseapp.com",
    "databaseURL": "https://realtimedbstoragedemo-2c0fb-default-rtdb.firebaseio.com",
    "projectId": "realtimedbstoragedemo-2c0fb",
    "storageBucket": "realtimedbstoragedemo-2c0fb.appspot.com",
    "messagingSenderId": "704263168946",
    "appId": "1:704263168946:web:47cd2accbeeeaa24813aab",
    "measurementId": "G-9TTEEPCR3G"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
storage = firebase.storage()

# name = input("Enter Name: ")
# age = input("Enter Age: ")
# profession = input("Enter Profession: ")

# filename = input("Enter the name of file you want to upload to storage: ")
# cloudfilename = input("Enter the name of the file in cloud: ")

# storage.child(cloudfilename).put(filename)
# url = storage.child(cloudfilename).get_url(None)
# data = {"Name": name, "Age": age, "Profession": profession, "url": url}
# db.child("users").push(data)


results = db.child("users").order_by_child("Name").equal_to("Harsh").get()
for result in results.each():
    # print(result.val()["url"])
    url = result.val()["url"]
    # print(result.key())
    f = urllib.request.urlopen(url).read() 
    print(f)