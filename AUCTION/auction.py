# -*- coding: utf-8 -*-
"""
Created on Tue May  2 09:29:32 2023

@author: fben-eghan
"""


class Player:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def __str__(self):
        return f"{self.name}: {self.budget}"

class Auction:
    def __init__(self, item, min_bid):
        self.item = item
        self.min_bid = min_bid
        self.bids = {}

    def add_bid(self, player, bid):
        if bid < self.min_bid:
            print(f"The minimum bid for this item is {self.min_bid}.")
            return False

        if self.item in self.bids and bid <= self.bids[self.item][0]:
            print(f"{player.name}: Your bid of {bid} is too low.")
            return False

        self.bids[self.item] = (bid, player)
        print(f"{player.name}: Your bid of {bid} is currently the highest bid for {self.item}.")
        return True

    def get_winner(self):
        if self.item in self.bids:
            return self.bids[self.item][1]
        else:
            return None

def run_auction(auction, players):
    print(f"Auctioning a {auction.item}. Minimum bid is {auction.min_bid}.")

    while True:
        # get player input
        player_name = input("Enter your name: ")
        if player_name == "":
            break

        # find player in players list
        current_player = None
        for player in players:
            if player.name == player_name:
                current_player = player
                break

        if not current_player:
            print("Unknown player.")
            continue

        # get bid input
        bid = int(input("Enter your bid: "))

        # check if bid is valid
        if not auction.add_bid(current_player, bid):
            continue

        # check if player has sufficient budget
        if current_player.budget < bid:
            print(f"{current_player.name}: You don't have enough budget for this bid.")
            continue
        current_player.budget -= bid

        # check if auction should end
        end_auction = input("Do you want to end the auction? (y/n) ")
        if end_auction.lower() == "y":
            winner = auction.get_winner()
            if winner:
                print(f"Auction ended. The {auction.item} sold for {auction.bids[auction.item][0]} to {winner.name}.")
                print("Current budgets:")
                for player in players:
                    print(player)
            else:
                print(f"Auction ended. No bids were made for the {auction.item}.")
            break
        else:
            print("Bidding continues.")

if __name__ == "__main__":
    players = [Player("Alice", 800), Player("Bob", 1000), Player("Charlie", 750)]
    auction = Auction("painting", 50)
    run_auction(auction, players)