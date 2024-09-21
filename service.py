from pymongo import MongoClient

mongo_uri = "mongodb+srv://vikasbmca:2021@cluster0.j8od8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(mongo_uri)
db = client['Python-Mongo']

collection = db['Python-Mongo-Collection']
def get_all_items():
    return list(collection.find({}, {'_id': 0}))

def add_item(item):
    result = collection.insert_one(item)
    return str(result.inserted_id)

