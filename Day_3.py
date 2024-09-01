print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island!! Your mission is to find the treasure.")

print("You are at the starting point. You have two directions to go. Hurry up and choose between left and right. Type \"left\" or \"right\".")

initial_direction = input().lower()

if initial_direction == "left":
    print("You walk in the direction of left for a while and reach a small lake. Do you want to swim or wait for someone? Type \"swim\" or \"wait\"")
    decision = input().lower()
    if decision == "wait":
        print("After waiting for some time, you realize there is a house-like structure near the bank. You go there to find three doors colored in red, blue and yellow. Choose a door. Type \"red\", \"blue\" or \"yellow\"")
        door = input().lower()
        if door == "yellow":
            print("YOU WINNNN!!!!. There is a big treasure lying the room and waiting for you.")
        if door == "red" or door == "blue":
            print("You encounter a murderer in the room. He stabs you continuously. You die. GAME OVER!")
    else:
        print("Oh Shit! There is a shark in the lake. You die. GAME OVER!")
else:
    print("Unforunately, there was a tiger in that direction. You die. GAME OVER!")

