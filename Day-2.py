# Tip Calculator
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))
payment = ((tip_percent/100 * total_bill)+total_bill) / num_people
print(payment)
# pre_payment = round(payment,2)
# print(pre_payment)
each_payment = "{:.2f}".format(payment)
print(type(each_payment))
print(f"Each person should pay: ${each_payment}")

