
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://jaij1660:pwskills@cluster0.l0buqvm.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
db=client.test
# Send a ping to confirm a successful connection
try:
    print(db)
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    
    #db=client['pwskills']

    # data ={"name" : 'jay',
    #    'meil_id' : 'jai@gmail.com',
    #    "ph_num" : 24356789 }

    # coll_pwskills=db["my_record"]

    # coll_pwskills.insert_one(data)



    db=client['pwskills']
    data1=[{'name':"pra",'id':'asfoieh@fja','time':"mor 4.35am",'num':34},
            {'name':'sita','id':'sarvji@famr','time':"mor 4.35am",'num':6789},
            {'name':'sak','id':'sam@Hste','time':"mor 4.35am",'num':567}]
    
    coll_pwskills=db["my_record"]

    coll_pwskills.insert_many(data1)

except Exception as e:
    print(e)
