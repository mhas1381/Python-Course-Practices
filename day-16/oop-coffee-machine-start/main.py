from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

cofee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while is_on:
    options = menu.get_items()
    user_choice = input(
        f"What would you like? {options}:\n").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        cofee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if cofee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            cofee_maker.make_coffee(drink)
