
import time
from tkinter import Menu

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
    "money" : 0
    }


def show_report():
    print("Water: {}ml".format(resources["water"]))
    print("Milk: {}ml".format(resources["milk"]))
    print("Coffee: {}ml".format(resources["coffee"]))
    print("Water: ${}".format(resources["money"]))

def check_ressources(ingredient_number):
    for i in ingredient_number:
        if ingredient_number[i] > resources[i]:
            print(f"Sorry, there is not enough {i}")
            return False
    return True

def drink_price():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def enough_money(payement, cost):
    if payement >= cost:
        change = round(payement - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Your money is being refunded as we speak.")
        return False

def making_coffee(name, ingredient_number):
    for i in ingredient_number:
        resources[i] -= ingredient_number[i]
    print(f"Here is your {name}. Enjoy!")


#START

machine_on = True


while machine_on:
    print("What would you like? (espresso/latte/cappuccino):")
    user_choice = input("--> ")

    if user_choice.strip().lower() == "report":
        show_report()

    elif user_choice.strip().lower() == "off":
        print("Turning off the coffee machine..")
        time.sleep(2)
        machine_on = False
    else:
        drink = MENU[user_choice]
        if check_ressources[drink["ingredients"]]:
            cost = drink_price()
            if enough_money(cost, drink["cost"]):
                making_coffee(user_choice, drink["ingredients"])
