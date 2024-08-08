import random

word_list = ["aardvark","baboon","camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = []

for n in range(len(chosen_word)):
    placeholder.append("_")
print("".join(placeholder))   


flag = True

while flag:
    if "_" in placeholder:
        guess = input("Guess a letter: ").lower()
        for n in range(len(chosen_word)):
            if chosen_word[n] == guess:
                placeholder[n] = guess
        print("".join(placeholder))
    else:
        break
print("You Wonn!")
