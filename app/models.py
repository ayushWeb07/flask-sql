# import packages
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    
    # instead of image → store timestamp
    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)

    views = db.Column(db.Integer, nullable=False, default=0)
    likes = db.Column(db.Integer, nullable=False, default=0)

    # author link
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
    username = db.Column(db.String(100), db.ForeignKey("user.username"), nullable=False)
    
    category_id = db.Column(db.Integer(), db.ForeignKey("category.id"), nullable=False)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password= db.Column(db.String(20), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)  # Boolean column

    

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
  