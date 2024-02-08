#!/usr/bin/env python3

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.sqlite3'
#
# db = SQLAlchemy(app)
# class Player(db.Model):


@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")

    return "Greeting: " + input_text


@app.route("/echo_nba", methods=["POST"])
def echo_nba_player():
    player_name = request.form.get("player_name", "")
    return "<p>Your favorite NBA player is: " + player_name + "</p>"


@app.route("/")
def main():
    return '''
    <h1>Enter a Greeting</h1>
    <form action="/echo_user_input" method="POST">
        <p>Enter a name or a sentence of your choosing.
        Soon this will be a website for NBA basketball players' metrics for stats gurus,
        fantasy players, or curiosity on a player's performance.

        <br>

        Suitable for fantasy drafts and trades, sports betting, statisticians, and gurus.
        In the meantime, enter a greeting to get started.
        </p>

        <input name="user_input">
        <input type="submit" value="Submit!">

    </form>

    <form action="/echo_nba" method="POST">
        <p>Who is your favorite NBA player?</p>
        <p>Preferably, enter a current player's name with first and last name.</p>  
        <input name="player_name">
        <input type="submit" value="Submit!">
    </form>
    '''

