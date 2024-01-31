#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def main():
    return '''
    <h1>Enter a Greeting</h1>
    <form action="/echo_user_input" method="POST">
        <p>Hello there! Enter a name or a sentence of your choosing. 
        Soon this will be a website for NBA basketball players' metrics for stats gurus, 
        fantasy players, or curiosity. 
        
        <br>
        
        Suitable for fantasy drafts and trades, sports betting, statisticians, and gurus. 
        In the meantime, enter a greeting to get started. 
        </p>
        
        <input name="user_input">
        <p>Who is your favorite NBA player?</p>     
        
        <input name="player_name">
        <input type="submit" value="Submit!">
    </form>
    '''


@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    player_name = request.form.get("player_name", "")
    return ("Greeting: " + input_text +
            "<p>Your favorite NBA player is: " + player_name + "</p>")
