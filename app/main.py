from werkzeug.utils import redirect
from flask_login import login_user
from app import app, login
from flask import render_template, request
from app.models import *
import hashlib


@app.route("/")
def index():
   return render_template("index.html")


@app.route("/login-nv", methods=["get", "post"])
def login_nv():
    return render_template("login-nv.html")


@app.route("/infostaff", methods=["get", "post"])
def info_staff():
    return render_template("infostaff.html")


@app.route("/home")
def home_us():
    return render_template("home.html")


@app.route("/login-admin", methods=["post", "get"])
def login_admin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password", "")
        password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
        user = User.query.filter(User.username == username.strip(),
                          User.password == password).first()
        if user:
            login_user(user=user)
    return redirect("/admin")


@login.user_loader
def user_loaf(user_id):
    return  User.query.get(user_id)


if __name__ == "__main__":
    app.run(debug=True, port=5555)