import random
from hangman_art import *
from hangman_words import word_list

print(logo)

chosen_word = random.choice(word_list)

placeholder = []

for n in range(len(chosen_word)):
    placeholder.append("_")
print("".join(placeholder))

currentStage = 6

while True:
    if "_" in placeholder and currentStage == 0:
        print("**********---You Lostt!!---**********")
        print(f"The word was {chosen_word.upper()}")
        break
    elif "_" in placeholder:
        guess = input("Guess a letter: ").lower()
        count = 0
        if guess in placeholder:
            print(f"You have already guessed {guess} before and it is in the list.")
        for n in range(len(chosen_word)):
            if chosen_word[n] == guess:
                placeholder[n] = guess
                count += 1
        if count == 0:
            currentStage -= 1
            print(f"Incorrect Guess!! You have {currentStage}/6 lives left.")
        else:
            print(f"Correct Guess!! You still have {currentStage}/6 lives left.")
        print("".join(placeholder))
        print(stages[currentStage])
    else:
        print("**********---You Wonn!!---**********")
        break

