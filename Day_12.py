import random

difficulty = input("Choose a difficulty between 'easy' and 'hard': ")
unknown_number = random.randint(1,100)


def is_guess_correct(num):
    guess_num = int(input("Make a guess: "))
    if guess_num == num:
        return 0
    else:
        if guess_num < num:
            return -1
        if guess_num > num:
            return 1

attempts = 0
if difficulty == "easy":
    attempts = 10
else:
    attempts = 5    

print(f"You have {attempts} attempts remaining to guess the number.")
    
while attempts != 0:
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
    print(f"You have {attempts} attempts remaining to guess the number.")

