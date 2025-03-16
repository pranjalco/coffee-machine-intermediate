import sys
from art import *
import time

"""
# Project 11: Coffee Machine
## Description:
This Coffee Machine project is a Python-based program that simulates a real-world coffee vending machine. 
It allows users to select from available drinks, processes payments, and dispenses coffee based on sufficient 
resources. It also includes functionality for resource management and a maintenance mode to check resources 
and earnings.

### Features:
- Simulates a coffee machine offering multiple drink options (espresso, latte, cappuccino).
- Validates user input for drink selection and payment.
- Calculates and processes payments using coins (quarters, dimes, nickels, pennies).
- Checks resource availability before making a drink.
- Tracks and updates resource levels after each use.
- Displays reports for resources and earnings in maintenance mode.
- Designed for interactive use in a command-line interface.

# Level: Intermediate
Author: Pranjal Sarnaik
Date: 2024-11-29
"""

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def add_blank_line():
    """This function adds blank line"""
    print("")


def user_coffee_choice():
    """This function asks user which coffee they want and return the user choice"""

    while True:
        add_blank_line()
        print("Type \nreport: to check available resources")
        print("owner: To check owner name")
        print("off: To turn off the coffee machine")
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input in ["espresso", "latte", "cappuccino"]:
            return user_input
        elif user_input == "off":
            turn_off_button()
        elif user_input == "report":
            show_report()
        elif user_input == "owner":
            print(f"Owner of machine is:")
            print(name())
        else:
            print("Please enter among given options: (espresso/latte/cappuccino)")
            add_blank_line()


# TODO: 2. Create Turn off option

def turn_off_button():
    """This function exits the program immediately whenever called"""
    add_blank_line()
    print(f"Turning off the coffee machine.")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Turned off 😿")
    time.sleep(1)
    add_blank_line()
    name_l()
    return sys.exit()


# TODO: 3. Print report
def show_report():
    """This function shows how much resources are remaining in machine for making coffee"""
    add_blank_line()
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")
    add_blank_line()


# TODO: 4. Check if there are enough resources present for making a drink


def coffee_item_list(coffee_name):
    """This function create variables based on user coffee choice and assign the values to those variables,
    e.g. for a coffee how many resources are required like milk, water, coffee and cost"""

    c_water = MENU[user_choice]["ingredients"]["water"]

    if coffee_name != "espresso":
        c_milk = MENU[user_choice]["ingredients"]["milk"]

    c_coffee = MENU[user_choice]["ingredients"]["coffee"]
    c_cost = MENU[user_choice]["cost"]

    if coffee_name != "espresso":
        return c_water, c_milk, c_coffee, c_cost
    else:
        return c_water, c_coffee, c_cost


def check_resources(u_choice, r_water, r_coffee, cof_water, cof_coffee, r_milk=0, cof_milk=0):
    """This function will check whether there will be enough resources present or not for making a coffee"""
    if u_choice != "espresso":
        water_flag = False
        coffee_flag = False
        milk_flag = False
        if r_water >= cof_water:
            water_flag = True
        else:
            print("Sorry there is not enough water.")

        if r_coffee >= cof_coffee:
            coffee_flag = True
        else:
            print("Sorry there is not enough coffee.")

        if r_milk >= cof_milk:
            milk_flag = True
        else:
            print("Sorry there is not enough milk.")

        if water_flag and coffee_flag and milk_flag:
            return True
        else:
            return False

    else:
        water_flag = False
        coffee_flag = False

        if r_water >= cof_water:
            water_flag = True
        else:
            print("Sorry there is not enough water.")

        if r_coffee >= cof_coffee:
            coffee_flag = True
        else:
            print("Sorry there is not enough coffee.")

        if water_flag and coffee_flag:
            return True
        else:
            return False


def customer_total_money_calculator():
    """This function will calculate total money given by customer and returns the total in $"""
    while True:
        try:
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))

            total = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
            return round(total, 2)

        except ValueError:
            print("Please enter integer values.")


def check_transaction_status(customers_money, coffee_cost_original, choice_of_user):
    """This function will check if money given by customer is sufficient ot not, if it is sufficient then it will
    give coffee to customer and if money given by customer is larger than the cost of coffee then in that case
    it will give back the change.
    Based on transaction it will return True or False"""
    if customers_money >= coffee_cost_original:
        change = customers_money - coffee_cost_original
        change = round(change, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        print(f"Here is your {choice_of_user} ☕️. Enjoy!")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def update_reports(user_choice_coffee):
    """This function will update resources data whenever coffee is made using required ingredients"""
    if user_choice_coffee != "espresso":
        resources["money"] += cofe_cost

        resources["water"] -= cofe_water
        resources["milk"] -= cofe_milk
        resources["coffee"] -= cofe_coffee
    else:
        resources["money"] += cofe_cost

        resources["water"] -= cofe_water
        resources["coffee"] -= cofe_coffee


while True:

    print(logo)
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]

    user_choice = user_coffee_choice()

    # -----------------------------------------------------------------------------------------------

    while True:

        if user_choice != "espresso":
            cofe_water, cofe_milk, cofe_coffee, cofe_cost = coffee_item_list(user_choice)

        else:
            cofe_water, cofe_coffee, cofe_cost = coffee_item_list(user_choice)

        if user_choice != "espresso":
            eligible = check_resources(user_choice, water, coffee, cofe_water, cofe_coffee, milk, cofe_milk)

        else:
            eligible = check_resources(user_choice, water, coffee, cofe_water, cofe_coffee, r_milk=0, cof_milk=0)

        if not eligible:
            user_choice = user_coffee_choice()
        else:
            break

    # -----------------------------------------------------------------------------------------------

    customer_money = customer_total_money_calculator()
    status = check_transaction_status(customer_money, cofe_cost, user_choice)
    if status:
        update_reports(user_choice)
