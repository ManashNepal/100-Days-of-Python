import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["aardvark","baboon","camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""

for n in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

listholder = list(placeholder)

currentStage = 6

while True:
    if "_" in listholder and currentStage == 0:
        print("You Lostt!!")
        break
    elif "_" in listholder:
        guess = input("Guess a letter: ").lower()
        count = 0
        for n in range(len(chosen_word)):
            if chosen_word[n] == guess:
                listholder[n] = guess
                count += 1
        if count == 0:
            currentStage -= 1
        print("".join(listholder))
        print(stages[currentStage])
    else:
        print("You Wonn!")
        break

