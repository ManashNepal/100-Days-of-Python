import os
from secret_auction_art import *

def get_highest_bidder(bid_dictionary):
    highest_bid = 0
    highest_bidder = ""

    for bidder in bid_dictionary:
        if bid_dictionary[bidder] > highest_bid:
            highest_bid = bid_dictionary[bidder]
            highest_bidder = bidder

    print(f"The winner is {highest_bidder} with a bid of Rs.{highest_bid}.")

print(logo)

bid_dictionary = {}
flag = True

while flag: 
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: Rs."))
    bid_dictionary[name] = bid
    decision = input("Are there other bidders(yes/no)?: ").lower()

    if decision == "no":
        flag = False
    
    os.system('cls')

get_highest_bidder(bid_dictionary)
