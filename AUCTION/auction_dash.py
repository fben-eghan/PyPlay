# -*- coding: utf-8 -*-
"""
Created on Tue May  2 10:36:27 2023

@author: fben-eghan
"""

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from auction import Player, Auction

# create players and auction
players = [Player("Alice", 800), Player("Bob", 1000), Player("Charlie", 750)]
auction = Auction("painting", 50)

# initialize Dash app
app = dash.Dash(__name__)

# define app layout
app.layout = html.Div([
    html.H1("Auction Game"),
    html.H2(f"Auctioning a {auction.item}. Minimum bid is {auction.min_bid}."),
    html.H3("Enter your name:"),
    dcc.Input(id="player-name", type="text", placeholder="Enter your name"),
    html.H3("Enter your bid:"),
    dcc.Input(id="bid-input", type="number", placeholder="Enter your bid"),
    html.Button("Submit Bid", id="submit-bid"),
    html.Div(id="output")
])

# define app callbacks
@app.callback(
    Output("output", "children"),
    Input("submit-bid", "n_clicks"),
    State("player-name", "value"),
    State("bid-input", "value")
)
def update_output(n_clicks, player_name, bid):
    if n_clicks is not None:
        # find player in players list
        current_player = None
        for player in players:
            if player.name == player_name:
                current_player = player
                break

        if not current_player:
            return html.Div("Unknown player.")

        # check if bid is valid
        if not auction.add_bid(current_player, bid):
            return html.Div(f"{current_player.name}: Your bid of {bid} is not valid.")

        # check if player has sufficient budget
        if current_player.budget < bid:
            return html.Div(f"{current_player.name}: You don't have enough budget for this bid.")

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

        return html.Div(output_text)

# run app
if __name__ == "__main__":
    app.run_server(debug=True)

