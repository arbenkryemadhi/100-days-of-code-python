from data import MENU


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def check_for_resources(drink):
    """Checks if there are enough resources for a drink."""

    # Each resource is associated with a number and then they are checked one by one.
    resource = {
        0: "water",
        1: "milk",
        2: "coffee",
    }
    for i in range(0, 3):
        if MENU[drink]["ingredients"][resource[i]] > resources[resource[i]]:
            print(f"Not enough {resource[i]} to make the drink.")
            return

    for i in range(0, 3):
        resources[resource[i]] -= MENU[drink]["ingredients"][resource[i]]

    return True


def money_counter(drink):
    global resources
    money_inserted = 0

    # Asks to insert coins and turns them to int.
    print("Please insert money:")
    penny = int(input("Inscert pennies: "))
    nickel = int(input("Inscert nickels: "))
    dime = int(input("Inscert dimes: "))
    quarter = int(input("Inscert quarters: "))

    # Calculates the sum of coins entered.
    money_inserted = penny * 0.01 + nickel * 0.05 + dime * 0.1 + quarter * 0.25

    if money_inserted < MENU[drink]["cost"]:
        print("Not enough money!")
    else:
        # Calculates the change that is going to be given back tot he user.
        change = money_inserted - MENU[drink]["cost"]
        print(f"Here is your change: {change}")

        # Puts the rest to its resources.
        resources["money"] = resources["money"] + money_inserted - change
        print


def machine():
    global resources

    # Gets input from user while making everything lowercase and interprets it
    user_input = input(
        "What would you like to get? (espresso / latte / cappuccino): ").lower()

    if user_input == "off":
        print("Turning Off!")
        return

    elif user_input == "report":
        # Prints a report of value of variables from global.
        print(f"""
            Water: {resources["water"]}ml
            Milk: {resources["milk"]}ml
            Coffee: {resources["coffee"]}g
            Money: ${resources["money"]}
            """)

    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        if check_for_resources(user_input):
            money_counter(user_input)

    else:
        print("Not a valid input!")

    machine()


machine()
