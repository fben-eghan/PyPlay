# -*- coding: utf-8 -*-
"""
Created on Tue May  2 10:36:27 2023

@author: fben-eghan
"""

from flask import Flask, render_template, request
from auction import Player, Auction
import webbrowser

url = 'http://127.0.0.1:5000/'

# create players and auction
players = [Player("Alice", 800), Player("Bob", 1000), Player("Charlie", 750)]
auction = Auction("painting", 50)

# initialize Flask app
app = Flask(__name__)

# define app routes
@app.route("/")
def index():
    return render_template("index.html", item=auction.item, min_bid=auction.min_bid)

@app.route("/", methods=["POST"])
def submit_bid():
    # get form inputs
    player_name = request.form.get("player-name")
    bid = int(request.form.get("bid-input"))

    # find player in players list
    current_player = None
    for player in players:
        if player.name == player_name:
            current_player = player
            break

    if not current_player:
        return "Unknown player."

    # check if bid is valid
    if not auction.add_bid(current_player, bid):
        return f"{current_player.name}: Your bid of {bid} is not valid."

    # check if player has sufficient budget
    if current_player.budget < bid:
        return f"{current_player.name}: You don't have enough budget for this bid."

    # update player budget
    current_player.budget -= bid

    # check if auction should end
    winner = auction.get_winner()
    if winner:
        output_text = f"Auction ended. The {auction.item} sold for {auction.bids[auction.item][0]} to {winner.name}.<br>"
        output_text += "Current budgets:<br>"
        for player in players:
            output_text += str(player) + "<br>"
    else:
        output_text = f"{current_player.name}: Your bid of {bid} is currently the highest bid for {auction.item}.<br>"
        output_text += "Bidding continues.<br>"

    return output_text

if __name__ == "__main__":
    app.run()
#webbrowser.open(url)
