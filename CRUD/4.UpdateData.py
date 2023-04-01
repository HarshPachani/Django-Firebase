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


"""#Insert data into firebase.
dataA = {
    "monday": {
                "paper": {
                            "deadline": "12pm",
                            "details": "firstsubmissior"
                        },
                "pull-request": {
                            "deadline": "3pm"
                        }
    },

    "tuesday": {
        "filmvideo": {"deadline": "N/A"}
    },

    "wednesday": {
        "project": {
                "deadline": "2am"
            },
            "volunteer":{
                "deadline": "9pm"
            } 
    }
}
"""
"""
paper = {"deadline": "12pm", "details": "firstsubmissior"}
pullrequest = {"deadline": "3pm"}

monday1 = {"deadline": "12pm", "name": "paper"}
monday2 = {"deadline": "3pm", "name": "pull-request"}
tuesday = {"deadline": "N/A", "name": "filmvideo"}
wednesday1 = {"deadline": "2am", "name": "project"}
wednesday2 = {"deadline": "2am", "name": "N/A"}

#set used for manual key
db.child("pyrebaserealtimedbdemo").child("todolistA").child("monday").child("paper").set(paper) 
db.child("pyrebaserealtimedbdemo").child("todolistA").child("monday").child("pull-request").set(pullrequest) 
db.child("pyrebaserealtimedbdemo").child("todolistA").child("tuesday").child("filmvideo").set({"deadline": "N/A"}) 
db.child("pyrebaserealtimedbdemo").child("todolistA").child("wednesday").child("project").set({"deadline": "2am"}) 
db.child("pyrebaserealtimedbdemo").child("todolistA").child("wednesday").child("volunteer").set({"deadline": "9pm"}) 

#push used for automatic generated key
db.child("pyrebaserealtimedbdemo").child("todolistB").child("monday").push(monday1)
db.child("pyrebaserealtimedbdemo").child("todolistB").child("monday").push(monday2)
db.child("pyrebaserealtimedbdemo").child("todolistB").child("tuesday").push(tuesday)
db.child("pyrebaserealtimedbdemo").child("todolistB").child("wednesday").push(wednesday1)
db.child("pyrebaserealtimedbdemo").child("todolistB").child("wednesday").push(wednesday2)
"""

# for Update data
# db.child("pyrebaserealtimedbdemo").child("todolistA").child("monday").child("paper").update({"deadline": "1pm"})

#for mass updating data
#Note: if you want to mass update then you have to also add those fields which you don't want to change otherwise it will deleted.
#Ex: Here we want to change details of todolistA/monday/paper but we also have to add deadline even we don't want deadline to change.
"""
data = {"pyrebaserealtimedbdemo/todolistA/monday/paper": {"details": "v2", "deadline": "12pm"}, 
        "pyrebaserealtimedbdemo/todolistA/tuesday/filmvideo": {"deadline": "7pm"}
    }

db.update(data)
"""

#To update an auto generated key data
monday_tasks = db.child("pyrebaserealtimedbdemo").child("todolistB").child("monday").get()

#To get the auto generated key first.
for task in monday_tasks.each(): #each is the function which helps to iterate
    # print(task.val())
    # print(task.key())

    #Now we will get the particular name's key here.
    if (task.val()['name'] == "paper"): #Getting the key of name = paper
        key = task.key()

db.child("pyrebaserealtimedbdemo").child("todolistB").child("monday").child(key).update({"deadline": "1pm"})