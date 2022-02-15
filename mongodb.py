from pymongo import MongoClient

MONGO_DB = "mongodb+srv://akalpana:akalpana@cluster0.xhmtq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

datab = MongoClient(MONGO_DB)
maindb = datab["main"]
usersdb = maindb["users"]
groupsdb = maindb["groups"]

def add_user(user_id):
    is_using = usersdb.find_one({"user_id": user_id})
    if is_using:
        return
    return usersdb.insert_one({"user_id": user_id}) 

def remove_user(user_id):
    is_using = usersdb.find_one({"user_id": user_id})
    if not is_using:
        return
    return usersdb.delete_one({"user_id": user_id})

def add_group(group_id):
    is_using = groupsdb.find_one({"group_id": group_id})
    if is_using:
        return
    return groupsdb.insert_one({"group_id": group_id}) 

def remove_group(group_id):
    is_using = groupsdb.find_one({"group_id": group_id})
    if not is_using:
        return
    return groupsdb.delete_one({"group_id": group_id})

def all_users():
    users = usersdb.find({})
    return users

def all_groups():
    groups = groupsdb.find({})
    gcount = len(list(groups))
    return gcount
