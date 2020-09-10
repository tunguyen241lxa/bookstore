from sqlalchemy.orm import relationship
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask import render_template
from werkzeug.utils import redirect

from app import db, admin
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, DateTime, Float, Date, ForeignKey, Boolean
from flask_login import current_user, logout_user


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

    def __str__(self):
        return self.name


class Bookcategory(db.Model):
    __tablename__ = "Bookcategory"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    products = relationship('Bookproduct', backref='Bookcategory', lazy=True)

    def __str__(self):
        return  self.name


class Bookproduct(db.Model):
    __tablename__ = "Bookproduct"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, default=0)
    image = Column(String(255), nullable=True)
    bookcategory_id = Column(Integer, ForeignKey(Bookcategory.id), nullable=False)

    def __str__(self):
        return  self.name



class Employee(db.Model):
    __tablename__ = "Employee"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    birthday = Column(Date, nullable=False)
    address = Column(String(255), nullable=False)
    position = Column(String(50), nullable=False)

    def __str__(self):
        return  self.name


class BookproductModelView(ModelView):
    column_display_pk = True
    can_create = True

    def is_accessible(self):
        return current_user.is_authenticated


class BookcategoryModelView(ModelView):
    column_display_pk = True
    can_create = True

    def is_accessible(self):
        return current_user.is_authenticated


class AboutUsView(BaseView):
    @expose("/")

    def index(self):
        return self.render("admin/about-us.html")

    def is_accessible(self):
        return current_user.is_authenticated


class LogoutView(BaseView):
    @expose("/")
    def index(self):
        logout_user()

        return redirect("/admin")

    def is_accessible(self):
        return current_user.is_authenticated


class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(BookcategoryModelView(Bookcategory, db.session))
admin.add_view(BookproductModelView(Bookproduct, db.session))
admin.add_view(AboutUsView(name="Thông Tin"))
admin.add_view(LogoutView(name="Đăng Xuất"))

if __name__ == "__main__":
    db.create_all()
