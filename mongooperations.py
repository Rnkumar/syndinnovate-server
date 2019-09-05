import pymongo as pm
mongo_client = pm.MongoClient("mongodb://localhost:27017/")


def insert_data(data):
    db = mongo_client["social-data"]
    user_collection = db["user_data"]
    data_collection = db["data"]
    name = data["name"]
    email = data["email"]
    user_data = {
        "name": name,
        "email": email
    }
    bulk_data = data
    user_id = user_collection.insert_one(user_data).inserted_id
    print(user_id)
    bulk_data["_id"] = user_id
    data_collection.insert_one(bulk_data)


if __name__ == "__main__":
    insert_data({
        "name": "Niresh",
        "email": "nireshkmr.raj@gmail.com",
        "facebook": {},
        "twitter": {},
        "sms": {},
        "pinterest": {},
        "apps": {}
    })


def get_users():
    db = mongo_client["social-data"]
    user_collection = db["user_data"]
    return user_collection.find()


def get_data(user_id):
    db = mongo_client["social-data"]
    # user_collection = db["user_data"]
    data_collection = db["data"]
    return data_collection.find_one(filter={"_id": user_id})