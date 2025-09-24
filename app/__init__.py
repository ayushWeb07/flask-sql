# import packages
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import db

# create the flask app and connect the app with the db
def create_app():
    
    # create app
    app= Flask(__name__)
    
    # DB connection with the app
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tweets.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "secret_goat"
    
    db.init_app(app)

    # import blueprints AFTER db.init_app
    from app.routes.auth import auth_bp
    from app.routes.tweets import tweets_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(tweets_bp)
    
    
    return app



