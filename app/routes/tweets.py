# import packages
from flask import Blueprint, request, url_for, Response, render_template, flash, session, redirect
from app.models import Tweet, Category
from app import db

# create the tweets blueprint
tweets_bp = Blueprint("tweets", __name__)


# get all tweets -> "/"
@tweets_bp.route("/")
def get_all_tweets():
    
    # user is not logged in
    if "username" not in session:
        flash("You must be logged in!", "error")
        return redirect(url_for("auth.login"))
    
    else:
        tweets= Tweet.query.all()
        categories= Category.query.all()
        
        return render_template("home.html",  tweets= tweets, categories= categories)
    
    
# get all categories -> "/categories"
@tweets_bp.route("/categories")
def get_all_categories():
    
    # user is not logged in
    if "username" not in session:
        flash("You must be logged in!", "error")
        return redirect(url_for("auth.login"))
    
    else:
        categories= Category.query.all()
        return render_template("categories.html",  categories= categories)
        
        
@tweets_bp.route("/category/<int:category_id>")
def tweets_by_category(category_id):

    # get all tweets belonging to this category
    tweets = Tweet.query.filter_by(category_id=category_id).order_by(Tweet.created_at.desc()).all()
    
    categories= Category.query.all()

    return render_template("home.html",  tweets= tweets, categories= categories)

        
# about -> "/about"
@tweets_bp.route("/about")
def show_about():
    
    # user is not logged in
    if "username" not in session:
        flash("You must be logged in!", "error")
        return redirect(url_for("auth.login"))
    
    return render_template("about.html")
        
        


# add tweet -> "/add"
@tweets_bp.route("/add", methods= ["POST"])
def add_tweet():
    
    # user is not logged in
    if "username" not in session :
        flash("You must be logged in!", "error")
        return redirect(url_for("auth.login"))
    
    else:
        
        # get the tweet details
        content= request.form.get("content")
        category_id= request.form.get("category_id")
        user_id= session["id"]
        username= session["username"]
        
            
        new_tweet= Tweet(content= content, user_id= user_id, category_id= category_id, username= username)
        db.session.add(new_tweet)
        db.session.commit()
        
        flash("Tweet succesfully added!", "success")
        
        return redirect(url_for("tweets.get_all_tweets"))
        

# update tweet: update tweet details
@tweets_bp.route("/update/<int:tweet_id>", methods= ["GET", "POST"])
def update_tweet(tweet_id):
        
    # get the tweet
    tweet= Tweet.query.get(tweet_id)
    
    if request.method == "GET" and tweet:
        return render_template("edit-tweet.html", tweet= tweet)
    
    elif request.method == "POST" and tweet:
        
        if request.form.get("content", None) is not None:
            tweet.content= request.form["content"]
            
        if request.form.get("likes", None) is not None:
            tweet.likes= request.form["likes"]
            
        db.session.commit()
        
        flash("Tweet details updated", "success")
            
        
    return redirect(url_for("tweets.get_all_tweets"))
    
        


# delete tweet
@tweets_bp.route("/delete/<int:tweet_id>", methods= ["POST"])
def delete_tweet(tweet_id):
    
    # get the tweet
    tweet= Tweet.query.get(tweet_id)
    
    if tweet:
        
        db.session.delete(tweet)
        db.session.commit()
                        
        
    return redirect(url_for("tweets.get_all_tweets"))


