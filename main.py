from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def make_coffee():
    """This function simulates the program one might see at a self dispensing coffee machine. """
    on = True

    # create objects
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while on:
        drink = input(f"What would you like? ({menu.get_items()}): ")
        if drink == "off":
            on = False
        elif drink == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            user_drink = menu.find_drink(drink)
            if user_drink:
                if coffee_maker.is_resource_sufficient(user_drink) and money_machine.make_payment(user_drink.cost):
                    order = coffee_maker.make_coffee(user_drink)


# potential modifications would be modifying this code to accept more than one drink, and of course adding tests, as
# well as adding error handling









make_coffee()
