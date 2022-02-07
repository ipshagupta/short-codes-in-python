MENU = {
    "Espresso": {
        "ingredients": {
            "water": 50,
            "milk": 60,
            "coffee": 18,
            "chocolate": 0,
            "hazelnut": 0,
        },
        "cost": 1.5,
    },
    "Latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
            "chocolate": 0,
            "hazelnut": 0,
        },
        "cost": 2.5,
    },
    "Cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
            "chocolate": 0,
            "hazelnut": 0,
        },
        "cost": 3.0,
    },
    "Hazelnut Latte": {
        "ingredients": {
            "water": 150,
            "milk": 100,
            "coffee": 20,
            "hazelnut": 20,
            "chocolate": 0,
        },
        "cost": 3.5,
    },
    "Hot Chocolate": {
        "ingredients": {
            "water": 0,
            "milk": 200,
            "coffee": 0,
            "hazelnut": 0,
            "chocolate": 100,
        },
        "cost": 3.5,
    }
}

resources = {
    "Water": 500,
    "Milk": 500,
    "Coffee": 200,
    "Chocolate": 300,
    "Hazelnut": 100,
    "Money": 0,
}


def display_resources():
    print("\n")
    for key in resources:
        if key == "Water" or key == "Milk" or key == "Hazelnut":
            print(f"{key} = {resources[key]} ml")
        elif key == "Money":
            print(f"{key} = ${resources[key]}")
        elif key == "Coffee" or key == "Chocolate":
            print(f"{key} = {resources[key]} gm")


def check_availability_of_drink(chosen_drink):
    for key in MENU:
        if key == chosen_drink:
            wt = MENU[key]['ingredients']['water']
            m = MENU[key]['ingredients']['milk']
            c = MENU[key]['ingredients']['coffee']
            h = MENU[key]['ingredients']['hazelnut']
            ch = MENU[key]['ingredients']['chocolate']

            if wt > resources['Water'] or m > resources['Milk'] or c > resources['Coffee'] or h > resources['Hazelnut'] or ch > resources['Chocolate']:
                return 0
            else:
                return 1


def calc_total_paid(q, d, n, p):
    t = q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01
    print(f"\nYou paid: ${t}")
    return t


def check_cost(given_total, drink_type):
    if given_total < MENU[drink_type]['cost']:
        print("\nInsufficient amount paid. Payment failed and refunded. Please order again.")
    else:
        if given_total > MENU[drink_type]['cost']:
            actual_cost = MENU[drink_type]['cost']
            change = given_total - actual_cost
            print(f"Change = ${change}")
            resources['Money'] += actual_cost
            resources['Water'] -= MENU[drink_type]['ingredients']['water']
            resources['Milk'] -= MENU[drink_type]['ingredients']['milk']
            resources['Coffee'] -= MENU[drink_type]['ingredients']['coffee']
            resources['Hazelnut'] -= MENU[drink_type]['ingredients']['hazelnut']
            resources['Chocolate'] -= MENU[drink_type]['ingredients']['chocolate']
        print("\nOrder successfully placed! Enjoy your drink and order again!")


keep_going = "yes"

while keep_going == "yes":
    
    print("\nWelcome to Starbucks Coffee.\n1. Place order\n2. Print Report")
    cus_choice = input("\nWhat would you like to do?\t").title()

    if cus_choice == "Place Order":
        print("\nDrinks available are: \n" + "\n".join(MENU.keys()))
        type_of_drink = input("What would you like to order?   ").title()

        available = check_availability_of_drink(type_of_drink)
        if available == 0:
            print("\nSorry, but this drink is not available at the moment. Please order something else.")
        elif available == 1:
            
            print(f"\nTotal cost of your drink: ${MENU[type_of_drink]['cost']}")

            print("Please pay below:")
            quarters = int(input("No. of quarters: "))
            dimes = int(input("No. of dimes: "))
            nickles = int(input("No. of nickles: "))
            pennies = int(input("No. of pennies: "))
            total = calc_total_paid(quarters, dimes, nickles, pennies)
            check_cost(total, type_of_drink)

    elif cus_choice == "Print Report":
        display_resources()

    keep_going = input("\nWould you like to go the start menu?   ")

