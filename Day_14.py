import random
import os
from higher_lower_data import data

logo = """
 _   _ _       _                 ___                            
| | | (_)     | |               / / |                           
| |_| |_  __ _| |__   ___ _ __ / /| |     _____      _____ _ __ 
|  _  | |/ _` | '_ \ / _ \ '__/ / | |    / _ \ \ /\ / / _ \ '__|
| | | | | (_| | | | |  __/ | / /  | |___| (_) \ V  V /  __/ |   
\_| |_/_|\__, |_| |_|\___|_|/_/   \_____/\___/ \_/\_/ \___|_|   
          __/ |                                                 
         |___/                                                  
"""
vs = """
____   ____     
\   \ /   /_____
 \   Y   /  ___/
  \     /\___ \ 
   \___//____  >
             \/ 
"""

def changeB():
    global A,B
    while A == B:
        B = random.choice(data)

def get_AB(score):
    global A, B
    if score == 0:
        A = random.choice(data)
    else:
        A = B
    B = random.choice(data)

    if A == B:
        changeB() 

def choice():
    print(f'Compare A: {A["name"]}, {A["description"]}, from {A["country"]}')
    print(vs)
    print(f'Against B: {B["name"]}, {B["description"]}, from {B["country"]}')
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    return choice

# Global Variables
A = {}
B = {}
score = 0
flag = True
print(logo)

while flag:
    get_AB(score)
    user_choice = choice()
    if (user_choice == "A" and A["follower_count"] > B["follower_count"]) or (user_choice == "B" and B["follower_count"] > A["follower_count"]):
        score += 1
        os.system('cls')
        print(logo)
        print(f"You're right! Current score: {score}")
    else:
        os.system('cls')
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        flag = False


