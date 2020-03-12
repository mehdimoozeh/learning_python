from pymongo import MongoClient

class RegisterModel:

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.sampleWeb
        self.Users = self.db.users

    def insert_user(self, username, password):
        _id = self.Users.insert({"username": username, "password": password})
        return _id