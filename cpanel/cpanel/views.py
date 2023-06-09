#This file is created by Harsh Pachani.
from django.shortcuts import render
import pyrebase
from django.contrib import auth

config = {
  'apiKey': "AIzaSyDfz4LXyaMzkjkS3JJHvAHbPsZpH7ymy6k",
  'authDomain': "cpanel-aaec2.firebaseapp.com",
  'databaseURL':"https://cpanel-aaec2-default-rtdb.firebaseio.com/",
  'projectId': "cpanel-aaec2",
  'storageBucket': "cpanel-aaec2.appspot.com",
  'messagingSenderId': "690093862161",
  'appId': "1:690093862161:web:b78ee0e2672104b7bbb0b0",
  'measurementId': "G-EHMCEEQQ7T"
}

firebase = pyrebase.initialize_app(config)
authentication = firebase.auth()
database = firebase.database()


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
    # auth.logout(request)
    try:
        del request.session['uId']
    except KeyError:
        pass
    return render(request, 'signIn.html')

def signUp(request):
    return render(request, 'signUp.html')

def postSignUp(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')

    try:
        user = authentication.create_user_with_email_and_password(email, password)
    except Exception as ex:
        message = f"unable to create account, Try again, :{ex}"
        return render(request, 'signIn.html', {"message": message})
    uId = user['localId']
    data = {"name": name, "status": "1"}
    idtoken = request.session['uid']
    d = database.child("users").child(uId).child("details").set(data, idtoken)
    print("\t\t\t\tData: ", d)
    return render(request, 'signIn.html')

def create(request):
    return render(request, 'create.html')

def post_create(request):
    import time
    from datetime import datetime, timezone
    import pytz

    """
        Note:When do you authenticate the user with the help of session then you have to change the rules of your firebase database
        Changes Rules:
        {
            "rules": {
                "users": {
                    "$uid": {
                        ".read": "$uid === auth.uid",
                        ".write": "$uid === auth.uid"
                    }
                }
            }    
                //These rules fetch the email id
        }
    """

    try:
        tz = pytz.timezone('Asia/kolkata')
        time_now = datetime.now(timezone.utc).astimezone(tz)
        millis = int(time.mktime(time_now.timetuple()))
        print("\t\t\t\t Mili: ", str(millis))

        work = request.POST.get('work')
        progress = request.POST.get('progress')

        idtoken = request.session['uid']
        a = authentication.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        a = a['localId']

        print("\t\t\t\tInfo: ", str(a))
        data = {
            "work": work,
            "progress": progress
        }


        database.child("users").child(a).child("reports").child(millis).set(data, idtoken) #This ,(comma) is important to authenticate the user.
        name = database.child("users").child(a).child("details").child("name").get(idtoken).val()
        return render(request, 'welcome.html', {"e": name})
    except KeyError:
        message= "Oops! User Logged out Please SignIn Again"
        return render(request, "signIn.html", {"message": message})
    
def check(request):
    import datetime

    idtoken = request.session['uid']
    a = authentication.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']

    timestamps = database.child("users").child(a).child("reports").shallow().get().val()
    print(timestamps)

    lis_time = []
    for i in timestamps:
        lis_time.append(i)
    lis_time.sort(reverse=True)
    print(lis_time)

    work = []
    for i in lis_time:
        wor = database.child("users").child(a).child("reports").child(i).child("work").get().val()
        work.append(wor)

    print(work)
    
    date = [] #For getting a date and time of the work assigned
    for i in lis_time:
        dat = datetime.datetime.fromtimestamp(i).strftime("%H:%M")


    return render(request, "check.html")

