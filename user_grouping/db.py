from pymongo import MongoClient
import json
from .schema_valid import post_validator, user_validator


def init_db():
  
  client = MongoClient("mongodb+srv://saif:brick@cluster0.j6jw7.mongodb.net/<dbname>?retryWrites=true&w=majority")

  db = client.user_grouping


  if db.Post:
    pass
  else:
    db.create_collection("Post", validator=post_validator)

  if db.users:
    pass
  else:
    db.create_collection("User", validator=user_validator)

  Post = db.Post
  User = db.User

  return db