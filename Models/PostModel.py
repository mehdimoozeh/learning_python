from pymongo import MongoClient
import datetime

class PostModel:

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.sampleWeb
        self.Posts = self.db.posts

    def insert_post(self, user, text):
        _id = self.Posts.insert({"user": user, "text": text, "createdAt": datetime.datetime.now()})
        return _id

    def find_user_posts(self, user):
        data = self.Posts.find({"user": user})
        return data