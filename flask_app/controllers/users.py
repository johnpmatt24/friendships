from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import friendship
from flask_app.models import user



@app.route("/")
def main():
    return redirect("/friendships")


@app.route("/friendships")
def friendships():
    return render_template("index.html", all_users = user.User.get_all(), all_friendships = friendship.Friendship.get_all_user_friendships())


@app.route("/create_user", methods = ["POST"])
def create():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
    }
    user.User.save(data)
    return redirect("/friendships")






@app.route("/create_friendship", methods = ["POST"])
def create_friendships():
    data = {
        "user_id" : request.form["user_id"],
        "friend_id" : request.form["friend_id"],
    }
    
    in_database = friendship.Friendship.get_friendship(request.form)
    if in_database:
        flash("already friends!")
        return redirect("/")
    
    if data["user_id"] == data["friend_id"]:
        flash("You can be friends with yourself!")
        return redirect("/friendships")

    friendship.Friendship.add_frienship(data)
    return redirect("/friendships")