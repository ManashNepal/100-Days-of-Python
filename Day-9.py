from secret_auction_art import *

print(logo)

bidder_info = {"Dummy":0}
flag = True

while flag:
    name = input("Enter the bidder name: ")
    bid = int(input("Enter your bid: $"))
    bidder_info[name] = bid
    decision = input("Are there other bidders(yes/no)?: ").lower()

    if decision == "no":
        flag = False


max_bidder = "Dummy"

for key in bidder_info:
    if bidder_info[key] > bidder_info[max_bidder]:
        max_bidder = key

print(f"The winner is {max_bidder} with a bid of ${bidder_info[max_bidder]}.")