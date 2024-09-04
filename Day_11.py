import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
exit_flag = True

while exit_flag:
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start_game == "y":
        computer = []
        player = []

        for n in range(2):
            player.append(random.choice(cards))
            computer.append(random.choice(cards))


        flag = True

        while flag:
            if sum(player) == 21:
                if sum(computer) == 21:
                    print(f"Your final hand: {player}, final score: {sum(player)}")
                    print(f"Computer's final hand: {computer}, final score: {sum(computer)}")
                    print("You loose!!")
                    flag = False
                else:    
                    print(f"Your final hand: {player}, final score: {sum(player)}")
                    print(f"Computer's final hand: {computer[0]}, final score: {computer[0]}")
                    print("You win!!")
                    flag = False
            print(f"Your cards: {player}, current score: {sum(player)}")
            print(f"Computer's first card: {computer[0]}")
            option = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if option == "y":
                player.append(random.choice(cards))
                print(f"Your cards: {player}, current score: {sum(player)}")
                print(f"Computer's first card: {computer[0]}")
                if sum(player)>21:
                    print("You went over. You lose!!")
                    flag = False
            else:
                while sum(computer)<17:
                    computer.append(random.choice(cards))
                    if sum(player) == sum(computer):
                        print(f"Your final hand: {player}, final score: {sum(player)}")
                        print(f"Computer's final hand: {computer}, final score: {sum(computer)}")
                        print("It's a draw!!")
                        break
                    elif sum(computer) == 21:
                        print(f"Your final hand: {player}, final score: {sum(player)}")
                        print(f"Computer's final hand: {computer}, final score: {sum(computer)}")
                        print("You loose!!")
                        break
                    elif sum(computer) > 21:
                        print(f"Your final hand: {player}, final score: {sum(player)}")
                        print(f"Computer's final hand: {computer}, final score: {sum(computer)}")
                        print("Opponent went over. You win!!")
                        break
                    elif sum(computer) > sum(player):
                        print(f"Your final hand: {player}, final score: {sum(player)}")
                        print(f"Computer's final hand: {computer}, final score: {sum(computer)}")
                        print("You loose!!")
                        break
                if sum(computer) < sum(player):
                    print(f"Your final hand: {player}, final score: {sum(player)}")
                    print(f"Computer's final hand: {computer}, final score: {sum(computer)}")
                    print("You win!!")
                else:
                    print(f"Your final hand: {player}, final score: {sum(player)}")
                    print(f"Computer's final hand: {computer}, final score: {sum(computer)}")
                    print("You loose!!")
                flag = False
    else:
        exit_flag = False