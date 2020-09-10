from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager
from flask_admin import Admin


app = Flask(__name__)
app.secret_key = "123456"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:1111@localhost/quanlynhasach?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

admin = Admin(app=app, name="QUẢN LÝ BÁN HÀNG", template_mode="bootstrap3")

login = LoginManager(app=app)