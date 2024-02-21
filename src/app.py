#!/usr/bin/env python3

from flask import Flask, request

from nba_api.stats.endpoints import playercareerstats, commonplayerinfo
from nba_api.stats.static import players


app = Flask(__name__)


# @app.route("/echo_user_input_player", methods=["POST"])
# def get_player_name_active():
#
#     user_input = request.form["user_input"]
#
#     nba_player = players.find_players_by_full_name(user_input)
#     if user_input != nba_player[0]['full_name']:
#         return "The player cannot be found. Please go back and try again."
#     else:
#         nba_player_career = playercareerstats.PlayerCareerStats(player_id=nba_player[0]['id'])
#         return nba_player_career.get_normalized_json()


# @app.route("/")
# def main():
#     return '''
#
#     <p>Hello there! Enter a name or a sentence of your choosing.
#         Soon this will be a website for NBA basketball players' metrics for stats gurus,
#         fantasy players, or curiosity.
#
#         <br>
#
#     <br>
#
#     You can check if the player you entered is active or not.
#     Enter the first AND last name and spell correctly. <br>
#     NOTE: We are working to get a drop down menu and/or features to search by last name.
#     <form action="/echo_user_input_player" method="POST">
#         <input name="user_input">
#         <input type="submit" value="Submit!">
#     </form>
#
#      '''


@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return "Greeting: " + input_text


@app.route("/")
def main():
    return '''Enter a greeting to get started.
        </p>

     <form action="/echo_user_input" method="POST">
         <input name="user_input">
         <input type="submit" value="Submit!">
     </form>
    '''


if __name__ == "__main__":
    app.run(debug=True)
    main()


'''
Really old code

 Suitable for fantasy drafts and trades, sports betting, statisticians, and gurus.
        In the meantime, enter a greeting to get started.
        </p>

     <form action="/echo_user_input" method="POST">
         <input name="user_input">
         <input type="submit" value="Submit!">
     </form>
    '''





