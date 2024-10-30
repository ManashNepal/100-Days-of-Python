with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_template:
    contents = letter_template.read()


for name in names:
    receiver = name.strip()
    new_contents = contents.replace("[name]",receiver)
    with open(f"./Output/ReadyToSend/letter_for_{receiver}.txt", mode="w") as ready_letters:
        letters = ready_letters.write(new_contents)