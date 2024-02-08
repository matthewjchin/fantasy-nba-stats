# #!/usr/bin/env python3
#
# from flask import Flask, request
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.sqlite3'
#
#
# @app.route("/")
# def main():
#     return '''
#     <h1>Enter a Greeting</h1>
#     <form action="/echo_user_input" method="POST">
#         <p>Hello there! Enter a name or a sentence of your choosing.
#         Soon this will be a website for NBA basketball players' metrics for stats gurus,
#         fantasy players, or curiosity on a player's performance.
#
#         <br>
#
#         Suitable for fantasy drafts and trades, sports betting, statisticians, and gurus.
#         In the meantime, enter a greeting to get started.
#         </p>
#
#         <input name="user_input">
#         <input type="submit" value="Submit!">
#
#     </form>
#
#     <form action="/echo_nba" method="POST">
#         <p>Who is your favorite NBA player?</p>
#         <input name="player_name">
#         <input type="submit" value="Submit!">
#     </form>
#     '''
#
#
# @app.route("/echo_user_input", methods=["POST"])
# def echo_input():
#     input_text = request.form.get("user_input", "")
#
#     return "Greeting: " + input_text
#
#
# @app.route("/echo_nba", methods=["POST"])
# def echo_nba_player():
#     player_name = request.form.get("player_name", "")
#     return "<p>Your favorite NBA player is: " + player_name + "</p>"
#


'''This is all test code. '''
# !/usr/bin/env python3
import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Weather.sqlite3'

'''
Define the database model
that is used to store 
the temperature.
'''

db = SQLAlchemy(app)


class Weather(db.Model):
    datetime = db.Column(db.DateTime, primary_key=True, default=datetime.utcnow())
    temperature = db.Column(db.Integer, nullable=False)


'''
Helper function to get temperature
using API
'''


def get_temperature():
    response = requests.get("https://weatherdbi.herokuapp.com/data/weather/boulder")
    return response.json()["currentConditions"]["temp"]["c"]


'''
In main we first get the current temperature and then 
create a new object that we can add to the database. 
'''
if __name__ == "__main__":
    current_temperature = get_temperature()
    new_entry = Weather(temperature=current_temperature)
    db.session.add(new_entry)
    db.session.commit()
