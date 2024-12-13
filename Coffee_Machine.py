from coffee_machine_data import *

def show_report():
    """Prints the current status of resources and money"""
    global money, water, milk, coffee
    amount = "{:.2f}".format(money)

    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${amount}")

def return_money(payment,coffee_type):
    """Calculate the money to be returned to the customer"""
    return_amount = payment - MENU[coffee_type]["cost"]
    return "{:.2f}".format(return_amount)

def use_resource():
    """Deduct the resources used while making a drink"""
    global money, water, milk, coffee
    money += MENU[coffee_type]["cost"]
    water -= MENU[coffee_type]["ingredients"]["water"]
    milk -= MENU[coffee_type]["ingredients"]["milk"]
    coffee -= MENU[coffee_type]["ingredients"]["coffee"]

#Important function
def make_coffee(coffee_type):
    """Makes the coffee asked by the customer and also checks if payment done is enough or not."""
    global money, water, milk, coffee
    payment = customer_payment()
    if payment >= MENU[coffee_type]["cost"]:
        if payment > MENU[coffee_type]["cost"]:
            print(f"Here is ${return_money(payment,coffee_type)} in change.")
        use_resource()
        print(f"Here is your {coffee_type}. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded")

def customer_payment():
    """Ask the user to pay in number of coins."""
    print("Please insert coins:-")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    total_payment = 0.25*quarters + 0.1*dimes + 0.05*nickels + 0.01*pennies
    return total_payment

def not_enough_resource(coffee_type):
    """Checks if the resources are enough or not"""
    global water, milk, coffee
    if MENU[coffee_type]["ingredients"]["milk"] > milk:
        print("Sorry there is not enough milk.")
        return True
    elif MENU[coffee_type]["ingredients"]["water"] > water:
        print("Sorry there is not enough water.")
        return True
    elif MENU[coffee_type]["ingredients"]["coffee"] > coffee:
        print("Sorry there is not enough coffee.")
        return True

money = 0
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
should_continue = True

while should_continue:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")

    if coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino":
        if not_enough_resource(coffee_type):
            continue
        else:
            make_coffee(coffee_type)
    if coffee_type == "off":
        should_continue = False
    if coffee_type == "report":
        show_report()
