alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceaser(direction,original_text,shift_amount):
    result = " "
    shifted_position = 0
    for letter in original_text:
        if letter == " ":
            pass
        else:
            if direction == "encode":
                shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet) 
            else:
              shifted_position = (alphabet.index(letter) - shift_amount)  
            result += alphabet[shifted_position]
    print(f"Here is the result: {result}")


    # if direction == "encode":
    #     encoded_code = ""
    #     for letter in original_text:
    #         if letter == " ":
    #             pass
    #         else:
    #             shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet) 
    #             encoded_code += alphabet[shifted_position]
    #     print(f"Here is the encoded result: {encoded_code}")
    # else:
    #     decoded_code = ""
    #     for letter in original_text:
    #         if letter == " ":
    #             pass
    #         else:
    #             shifted_pos = alphabet.index(letter) - shift_amount
    #             decoded_code += alphabet[shifted_pos]
    #     print(f"Here is the decoded result: {decoded_code}")


ceaser(direction=direction,original_text=text,shift_amount=shift)