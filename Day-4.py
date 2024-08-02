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

if user_choice>2 or user_choice<0:
    print("You typed an invalid number.")
    quit()
else:
    print(f"You have chosen {options_name[user_choice]} {options[user_choice]}")

randomizer = random.randint(0,2)

print(f"The computer has chosen {options_name[randomizer]} {options[randomizer]}")

if user_choice == 0 and randomizer == 2:
    print("You win!")
elif user_choice == 2 and randomizer == 0:
    print("You loose!")
elif user_choice > randomizer:
    print("You win!")
elif user_choice < randomizer:
    print("You loose!")
