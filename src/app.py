#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def main():
    return '''
     <form action="/echo_user_input" method="POST">
     <p>Hello there! Enter a name or a sentence of your choosing. 
     Soon this will be a website for NBA players' metrics for stats gurus, fantasy players, or curiosity. </p>
         <input name="user_input">
         <input type="submit" value="Submit!">
    <p>Who is your favorite NBA player?</p>     
        <input name="player_name">
        <input type="submit" value="Add">
     </form>
     '''


@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    player_name = request.form.get("player_name", "")
    return "You entered: " + input_text + " and your favorite NBA player is: " + player_name
