from random import choice

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True
main = Menu()

while is_on:
    option = main.get_items()
    choice = input(f"What would you like ({option}): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = main.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
           print (money_machine.make_payment(drink.cost))









