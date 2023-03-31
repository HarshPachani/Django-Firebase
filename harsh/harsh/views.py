from django.shortcuts import render
import pyrebase

config = {
    "apiKey": "AIzaSyD_mz8jeSn6CWqzu7VxRyps4G3z8DsKElQ",
    "authDomain": "connectingfirebasedbtopy-313fc.firebaseapp.com",
    "databaseURL": "https://connectingfirebasedbtopy-313fc-default-rtdb.firebaseio.com",
    "projectId": "connectingfirebasedbtopy-313fc",
    "storageBucket": "connectingfirebasedbtopy-313fc.appspot.com",
    "messagingSenderId": "654851677211",
    "appId": "1:654851677211:web:a38e9bd82ac3847a9e6cbe",
    "measurementId": "G-M28NXQ451K"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def home(request):
    channel_name = database.child("Data").child("Name").get().val()
    channel_type = database.child("Data").child("Type").get().val()
    channel_subs = database.child("Data").child("Subscribers").get().val()

    return render(request, 'index.html', {
        "channel_name": channel_name,
        "channel_type": channel_type,
        "channel_subscribers": channel_subs
    })

    print("\t\t\t\tChannel Name:", channel_name)
    print("\t\t\t\tChannel Type:", channel_type)
    print("\t\t\t\tChannel Subs:", channel_subs)