from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_on = True

while is_on:

    user_choice = input(f"What would you like? ({menu.get_items()}): ")

    if user_choice == "off":
        is_on = False
    
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        try:
            user_drink  = menu.find_drink(user_choice)
        
            if(coffee_maker.is_resource_sufficient(user_drink)):
                if(money_machine.make_payment(user_drink.cost)):
                    coffee_maker.make_coffee(user_drink)
        except Exception:
            continue