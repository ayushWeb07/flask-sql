# import packages
from app import create_app, db

# instantiate the app
app= create_app()

# instantiate the db
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(port= 8000, debug= True)