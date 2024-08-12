alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text,shift_amount):
    text_list = list(original_text)
    for letter in text_list:
        alphabet_index = alphabet.index(letter) 
        new_char = alphabet[(alphabet_index+shift_amount)%26]
        list_index = text_list.index(letter)
        text_list[list_index] = new_char
    print("".join(text_list))

encrypt(text,shift)