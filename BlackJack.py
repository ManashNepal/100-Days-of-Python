import random
import blackjack_art as art
import os

def deal_card():
    """Return a random card from a deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_score, computer_score):
    """Takes user's score and computer's score and return a winner"""
    if user_score == computer_score:
        print("It's a draw!")
    elif computer_score == 0:
        print("Computer wins with a blackjack!!!")
    elif user_score == 0:
        print("You win with a blackjack!!!")
    elif user_score > 21:
        print("You went over. You loose!!!")
    elif computer_score > 21:
        print("Computer went over. You win!!!")
    elif user_score > computer_score:
        print("You win!!!")
    else:
        print("You loose!!!")
    


play_again = True

while play_again:
    play_again_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = - 1
    is_game_over = False

    if play_again_choice == "n":
        play_again = False
    else:
        os.system("cls")
        print(art.logo)
        for n in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

        while not is_game_over:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)

            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            if user_score == 21 or computer_score == 21 or user_score > 21:
                is_game_over = True
            else:     
                choice = input("Type 'y' to get another card, type 'n' to pass: ")
                if choice == 'y':
                    user_cards.append(deal_card())
                else:
                    is_game_over = True

        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand {computer_cards}, final score: {computer_score}")    

        compare(user_score,computer_score)

    