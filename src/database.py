#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.sqlite3'

db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column("User_ID", db.integer, primary_key=True)
    name = db.Column(db.String(20))

