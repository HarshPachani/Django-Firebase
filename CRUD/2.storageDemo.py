import pyrebase
import urllib

firebaseConfig = {
    "apiKey": "AIzaSyDSLcLu6GSxece0XVRLZKIvwQk9qx1t4BU",
    "authDomain": "authdemo-91b1a.firebaseapp.com",
    "projectId": "authdemo-91b1a",
    "storageBucket": "authdemo-91b1a.appspot.com",
    "messagingSenderId": "769208992989",
    "appId": "1:769208992989:web:7e40535e9201a0c00f4734",
    "measurementId": "G-56WFZTBLVL"
}

firebase = pyrebase.initialize_app(firebaseConfig)

#Setting up storage
storage = firebase.storage()

"""
#Upload a file to storage
file = input("Enter the name of file you want to enter to the storage: ")
cloudFileName = input("Enter the name for the file and storage: ")
storage.child(cloudFileName).put(file)

#get file url
print(storage.child(cloudFileName).get_url(None))
"""

"""
#Download File
downloadLink = input("Enter Download URL: ")
filename = "download.txt"
storage.child(downloadLink).download(filename, "Download.txt")
"""

#Read from a file
path = input("Enter the path of the storeage you want to read: ")
print(storage.child(path).get_url(None))
url = storage.child(path).get_url(None)
f = urllib.request.urlopen(url).read() #To read file from the web url.
print(f)
