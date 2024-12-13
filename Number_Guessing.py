import random

#It is a way to create global constant like for PI = 3.14
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def is_guess_correct(num):
    guess_num = int(input("Make a guess: "))
    if guess_num == num:
        return 0
    else:
        if guess_num < num:
            return -1
        if guess_num > num:
            return 1

print("Welcome to the Number Guessing Game!!")
print("I'm thinking of a number between between 1 and 100.")
unknown_number = random.randint(1,100)
difficulty = input("Choose a difficulty between 'easy' and 'hard': ")

attempts = 0
if difficulty == "easy":
    attempts = EASY_LEVEL_ATTEMPTS
else:
    attempts = HARD_LEVEL_ATTEMPTS    
    
while True:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = is_guess_correct(unknown_number)
    attempts -= 1   
    if guess == 0 :
        print(f"You got it! The answer was {unknown_number}.")
        break
    if guess == -1:
        print("Too low.")
    if guess == 1:
        print("Too high.")
    if attempts == 0:
        print(f"You've run out of guesses, you loose.")
        break
    print("Guess again.")
    

