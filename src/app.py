#!/usr/bin/env python3

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from nba_api.stats.endpoints import playercareerstats, commonplayerinfo
from nba_api.stats.static import players

# import nba_api
import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.sqlite3'

db = SQLAlchemy(app)


@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return "Greeting: " + input_text


@app.route("/echo_user_input_player", methods=["POST"])
def get_player_name_active():

    user_input = request.form["user_input"]

    nba_player = players.find_players_by_full_name(user_input)
    if user_input != nba_player[0]['full_name']:
        # custom_headers = {
        #     'Host': 'stats.nba.com',
        #     'Connection': 'keep-alive',
        #     'Cache-Control': 'max-age=0',
        #     'Upgrade-Insecure-Requests': '1',
        #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        #     'Accept-Encoding': 'gzip, deflate, br',
        #     'Accept-Language': 'en-US,en;q=0.9',
        # }
        #
        # player_common_info = commonplayerinfo.CommonPlayerInfo(player_id=nba_player.get('id'),
        #     proxy='127.0.0.1:80', headers=custom_headers, timeout=600)
        #
        # return str(player_common_info.get_response())
        return "The player cannot be found. Please go back and try again."
    else:
        nba_player_career = playercareerstats.PlayerCareerStats(player_id=nba_player[0]['id'])

        return nba_player_career.get_normalized_json()


@app.route("/")
def main():
    return '''
        <p>Hello there! Enter a name or a sentence of your choosing.
            Soon this will be a website for NBA basketball players' metrics for stats gurus,
            fantasy players, or curiosity.
        </p>

        <p>
            Suitable for fantasy drafts and trades, sports betting, statisticians, and gurus.
            In the meantime, enter a player's name or a greeting to get started.           
        </p>
        <form action="/echo_user_input" method="POST">
            <input name="user_input">
            <input type="submit" value="Submit!">
        </form>
        
        You can check if the player you entered is active or not. Enter the first AND last name. <br>
        <form action="/echo_user_input_player" method="POST">
            <input name="user_input">
            <input type="submit" value="Submit!">
        </form>
        '''


if __name__ == "__main__":
    app.run(debug=True)
    main()


