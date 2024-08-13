from caesar_art import logo
print(logo)

def caeser(direction,original_text,shift_amount):
    result = " "
    shifted_position = 0
    for letter in original_text:
        if letter not in alphabet:
            result += letter
        else:
            if direction == "encode":
                shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet) 
            else:
              shifted_position = (alphabet.index(letter) - shift_amount)  
            result += alphabet[shifted_position]
    print(f"Here is the {direction}d code: {result}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
flag = True

while flag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(direction=direction,original_text=text,shift_amount=shift)
    decision = input("Do you want to continue? (Y/N):\n").lower()
    if decision == "n":
        flag = False
        print("Thank you for using our program!!")