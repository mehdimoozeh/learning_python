from pymongo import MongoClient

class RegisterModel:

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.sampleWeb
        self.Users = self.db.users

    def insert_user(self, username, password, fullname):
        _id = self.Users.insert({"username": username, "password": password, "fullname": fullname})
        return _id