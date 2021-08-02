from pymongo import MongoClient
import random
import string
import time

def randomString(stringLen=10, num = 10):
    random.seed(1)
    keyValRS = []
    for x in range(num):
        lett = string.ascii_lowercase
        keyValRS.append(''.join(random.choice(lett) for i in range(stringLen)))
    return keyValRS

def experiment(num):
    try:
        conn = MongoClient('192.168.122.240',27017)
        print("MongoDB Connected successfully!!")
    except:
        print("Could not connect to MongoDB")

    # database
    db = conn.test
    collection = db.yash
    lett = string.ascii_lowercase

    keyrs = randomString(10, num)
    valuers = randomString(90, num)

    #Insert Record
    start_time=time.time()
    for i, key in enumerate(keyrs):
        value = valuers[i]
        key_val = {
                "_id":key,
                "value":valuers[i]
            }
        print(key)
        rec_id = collection.insert_one(key_val)
    elapsed_time=time.time()-start_time
    print("Insert Time: ", elapsed_time)

    #Query Record
    start_time = time.time()
    for key in keyrs:
        rec_id = collection.find({"_id":key})
        for x in rec_id:
            print(x)
    elapsed_time = time.time()-start_time
    print("Lookup Time: ", elapsed_time)

    #Delete Record
    start_time = time.time()
    for key in keyrs:
        print(key)
        rec_id = collection.delete_one({"_id":key})

    elapsed_time = time.time()-start_time
    print("Delete Time", elapsed_time)


experiment(10000)

