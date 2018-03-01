import pymongo
import private

from pymongo import MongoClient
from bson.objectid import ObjectId

#connectString = "mongodb://{u}:{p}@ds249418.mlab.com:49418/cloudapps"
connectString = "mongodb://Admin:slickrick@ds249418.mlab.com:49418/cloudapps"
#connectString = connectString.format(u=private.mongo_username, p=private.mongo_password)
client = MongoClient(connectString)

def get_tasks():
    client = MongoClient(connectString)

    db = client.cloudapps
    current_tasks = db['tasks']

    tasks = list(current_tasks.find())
    for task in tasks:
        task['_id'] = str(task['_id'])
    client.close()
    return tasks

def get_tasks_by_status(status):
    client = MongoClient(connectString)

    db = client.cloudapps
    current_tasks = db.tasks

    tasks = list(current_tasks.find({"status":status}))
    for task in tasks:
        task['_id'] = str(task['_id'])
    client.close()
    return tasks

def get_task(task_id):
    client = MongoClient(connectString)

    db = client.cloudapps
    current_tasks = db.tasks



    # Convert from string to ObjectId:
    object_id = ObjectId(task_id)
    task = current_tasks.find_one({'_id': object_id})
    task['_id'] = str(task['_id'])
    client.close()
    return task

def save_task(task):
    client = MongoClient(connectString)

    db = client.cloudapps
    current_tasks = db.tasks
    task_id = current_tasks.insert_one(task).inserted_id
    client.close()
    return str(task_id)

def delete_task(task_id):
    client = MongoClient(connectString)

    db = client.cloudapps
    current_tasks = db.tasks
    object_id = ObjectId(task_id)
    task = current_tasks.delete_one({'_id': object_id})

def update_task(task_id, description=None, status=None):
    client = MongoClient(connectString)

    db = client.cloudapps
    current_tasks = db.tasks
    if description:
        update = {'$set':{'description':description}}
        object_id = ObjectId(task_id)
        current_tasks.update_one({'_id': object_id}, update)
    if status:
        update = {'$set':{'status':status}}
        object_id = ObjectId(task_id)
        current_tasks.update_one({'_id': object_id}, update)
    client.close()


