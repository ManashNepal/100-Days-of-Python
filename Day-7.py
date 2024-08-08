import random

word_list = ["aardvark","baboon","camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""

for n in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

listholder = list(placeholder)


while True:
    if "_" in listholder:
        guess = input("Guess a letter: ").lower()
        for n in range(len(chosen_word)):
            if chosen_word[n] == guess:
                listholder[n] = guess
        print("".join(listholder))
    else:
        break
print("You Wonn!")
