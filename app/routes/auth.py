# import packages
from flask import Blueprint, request, url_for, Response, render_template, flash, session, redirect
from app.models import User
from app import db


# create the auth blueprint
auth_bp = Blueprint("auth", __name__)


# admin credentials
admin_credentials= {
    "username" :"admin",
    "password" :"admin"
}



# handle register -> "/register"
@auth_bp.route("/register", methods= ["GET", "POST"])
def register():

    # user is posting the credentials
    if request.method == "POST":
        
        # get the username and the password
        username= request.form.get("username")
        password= request.form.get("password")
        
            
        session["username"]= username
        session["password"]= password
        
        if(username == admin_credentials["username"] and password == admin_credentials["password"]):
            session["is_admin"]= True
            
        else:
            session["is_admin"]= False
            
            
        newUser = User(username= username, password= password, is_admin= session["is_admin"])
        
        
        
        db.session.add(newUser)
        db.session.commit()
        
        session["id"]= newUser.id
            
        return redirect(url_for("tweets.get_all_tweets"))
            
        
    # render the register page if the user just wants to get the register page
    else:
        return render_template("register.html")

# handle login -> "/login"
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # get the credentials from the form
        username = request.form.get("username")
        password = request.form.get("password")

        # query the user from the database
        user = User.query.filter_by(username=username).first()

        # check if user exists and password matches
        if user and user.password == password:
            session["username"] = username
            session["password"] = username
            
            if(username == admin_credentials["username"] and password == admin_credentials["password"]):
                session["is_admin"]= True
                
            else:
                session["is_admin"]= False
                
            session["id"]= user.id
            
            return redirect(url_for("tweets.get_all_tweets"))  # redirect to dashboard or tweets page
        else:
            error = "Invalid username or password"
            return render_template("login.html", error=error)

    # render the login page if GET request
    else:
        return render_template("login.html")
    


# handle logout -> "/logout"
@auth_bp.route("/logout")
def logout():
    
    # remove the saved credentials from the session
    session.pop("username", None)
    session.pop("password", None)
    session.pop("is_admin", None)
    session.pop("id", None)
        
    return redirect(url_for("auth.login"))
    
    
    
    