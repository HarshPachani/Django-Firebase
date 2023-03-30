import pyrebase

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
auth = firebase.auth()

#email: dummymail@gmail.com
#pass: fakepass

#email: harsh@gmail.com
#pass: harshharsh

def signUp():
    print("Signing up...")
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print("Successfully Created account")
        ask = input("Do You want to login now? [y/n]")
        if ask == "y":
            login()
    except:
        print("Email Already Exists")

def login():
    print("Logging in...")
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print("Successfully Logged in!")
        print(auth.get_account_info(login['idToken']))
    except:
        print("Invalid Email or Password!")

ans = input("Are you a new user?[y/n]")
if ans == "y":
    signUp()
elif ans == "n":
    login()