import pymongo

from Student import Student
import json

class student_service:
    def insert_mongo(self, student):
         connection_url = "mongodb+srv://vikasbmca:3020@cluster0.uv1hh3c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
         client = pymongo.MongoClient(connection_url)

         db = client['Python-Mongo']

         collection = db['Python-Mongo-Collection']
         collection.insert_one(student)