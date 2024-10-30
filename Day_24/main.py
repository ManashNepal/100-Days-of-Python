with open("Day_24/Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("Day_24/Input/Letters/starting_letter.txt") as letter_template:
    contents = letter_template.read()


for name in names:
    receiver = name.strip()
    new_contents = contents.replace("[name]",receiver)
    with open(f"Day_24/Output/ReadyToSend/{receiver}.txt", mode="w") as ready_letters:
        letters = ready_letters.write(new_contents)