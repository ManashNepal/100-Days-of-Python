import pandas

nato_phonetic_df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_phonetic_dict = {row["letter"]:row["code"] for (index, row) in nato_phonetic_df.iterrows()}

user_input = input("Enter a word: ")

result = [nato_phonetic_dict[item.upper()] for item in list(user_input)]

print(result)
    