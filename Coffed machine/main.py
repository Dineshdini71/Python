MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    # is_enough = True  "For Understanding Purpose"
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False  # is_enough = False
    return True   # is_enough = True

def process_coin():
    print('Please insert the coin')
    total = int(input("how many quarters? ")) * 0.25
    total += int(input("how many dimes? ")) * 0.01
    total += int(input("how many nickles? ")) * 0.05
    total += int(input("how many pennies? ")) * 0.1
    return total

def transaction_successful(money_received, drink_cost):
    change = round(money_received - drink_cost, 2)
    print(f'Here is {change} in change')
    global profit
    profit += drink_cost
    if money_received >= drink_cost:
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} 🍵 Enjoy!")


# TODO 1. Print report of all coffee machine resources.
is_on = True
while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        is_resource_sufficient(drink["ingredients"])
        payment = process_coin()
        transaction_successful(payment, drink["cost"])
        make_coffee(choice, drink["ingredients"])


"""
* So this style of programming is called Procedural.
* Procedural programming is one of the earliest paradigms of Programming.
* In fact, back in the days when we had older languages like Fortran and COBOL,
"""