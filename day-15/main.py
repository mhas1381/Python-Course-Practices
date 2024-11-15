from data import MENU, resources

is_on = True


def report(resources):
    for key in resources:
        print(f" {key} : {resources[key]}")


def check_resources(resources, cofee_type):
    value = MENU[cofee_type]["ingredients"]
    for ingredient in value:
        if value[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        else:
            return True


def process_coins():
    money = 0
    print("Please insert coins")
    coins = {"quarters": 0.25,
             "dimes": 0.10,
             "nickles": 0.05,
             "pennies": 0.01}
    for coin in coins:
        count = int(input(f"How many {coin} : "))
        money += count * coins[coin]
    print(money)



while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino):\n").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        report(resources)
    else:
        check_resources(resources, user_choice)
        process_coins()
