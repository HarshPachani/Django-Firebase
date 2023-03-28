#This file is created by Harsh Pachani.
from django.shortcuts import render
import pyrebase
from django.contrib import auth

config = {
  'apiKey': "AIzaSyDfz4LXyaMzkjkS3JJHvAHbPsZpH7ymy6k",
  'authDomain': "cpanel-aaec2.firebaseapp.com",
  'projectId': "cpanel-aaec2",
  'storageBucket': "cpanel-aaec2.appspot.com",
  'messagingSenderId': "690093862161",
  'appId': "1:690093862161:web:b78ee0e2672104b7bbb0b0",
  'measurementId': "G-EHMCEEQQ7T"
}

firebase = pyrebase.initialize_app(config)
authentication = firebase.auth()

#This is a view
def signIn(request):
    return render(request, 'signIn.html')

def postSign(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    try:
        user = authentication.sign_in_with_email_and_password(email, password)
    except:
        message = "Invalid Credentials"
        return render(request, 'signIn.html', {"message": message})
    
    print("\t\t\t\t", user['idToken'])
    session_id = user['idToken']
    request.session['uid'] = str(session_id)

    return render(request, 'welcome.html', {"e":email})

def logout(request):
    auth.logout(request)
    return render(request, 'signIn.html')