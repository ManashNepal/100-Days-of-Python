def life_in_weeks(age):
    remaining_years = 90-age
    remaining_weeks = remaining_years * 52
    print(f"You have {remaining_weeks} left.")


age = int(input())
life_in_weeks(age)