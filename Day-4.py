import random

Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")



options = [Rock, Paper, Scissors]
options_name = ["Rock", "Paper", "Scissors"]

user_choice = int(input("Choose between Rock(0), Paper(1), Scissors(2): "))

print(f"You have chosen {options_name[user_choice]} \n {options[user_choice]}\n")

randomizer = random.randint(0,2)

print(options[randomizer])
print(f"The computer has chosen {options_name[randomizer]}")

if options_name[user_choice] == "Rock" and options_name[randomizer] == "Scissors":
    print("You win the game!")
elif options_name[user_choice] == "Scissors" and options_name[randomizer] == "Paper":
    print("You win the game!")
elif options_name[user_choice] == "Paper" and options_name[randomizer] == "Rock":
    print("You win the game!")
elif options_name[user_choice] == "Scissors" and options_name[randomizer] == "Rock":
    print("You loose the game!")
elif options_name[user_choice] == "Paper" and options_name[randomizer] == "Scissors":
    print("You loose the game!")
elif options_name[user_choice] == "Rock" and options_name[randomizer] == "Paper":
    print("You loose the game!")
else:
    print("Its a draw!!")

