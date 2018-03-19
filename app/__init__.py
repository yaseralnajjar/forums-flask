from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

folder_path = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = f"""sqlite:///{os.path.join(folder_path, "my_database.db")}"""
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

from app import stores, dummy_data

member_store = stores.MemberStore()
post_store = stores.PostStore()
dummy_data.seed_stores(member_store, post_store)

from app import views
from app import api
