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

def resources_sufficient():
    for i in user_ingredients:
        if user_ingredients[i] > resources[i]:
            print(f"Sorry there is not enough {i}")
            return False
    return True

def sum_coins():
    sum_all = 0
    coins_dic = {
    "quarters" : 0.25,
    "dimes" : 0.10,
    "nickles" : 0.05,
    "pennies" : 0.01,
}
    print("Please insert coins.")
    for coin in coins_dic:
        how_much = int(input(f"how many {coin}?: "))
        how_much = how_much * coins_dic[coin]
        sum_all += how_much
    return round(sum_all, 2)

def compare(the_sum):
    value = MENU[chose]["cost"]
    back = the_sum - value
    if the_sum != value:
        if the_sum > value:
            return True , f"Here is ${round(back, 2)} in change.", value
        elif the_sum < value:
            return False , "That's not enough", 0
    else:
        return True, "", value

def reduce_resources():
    for i in user_ingredients:
        guess_value = user_ingredients[i]
        value = resources[i] - guess_value
        resources[i] = value
    return resources

turn_off = True
while turn_off:
    chose = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if chose == "off":
        turn_off = False
    elif chose == "report":
        for item in resources:
            print(f"{item}: {resources[item]}")
        print(f"money: {profit}")
    elif chose not in MENU:
        print("Sorry, that is not a valid choice.")
    else:
        user_ingredients = MENU[chose]["ingredients"]
        status = resources_sufficient()
        if status:
            status_payment , message , drink_cost = compare(sum_coins())
            if not status_payment:
                print(message)
            else:
                profit += drink_cost
                reduce_resources()
                print(message)
                print(f"Here is your {chose} ☕️. Enjoy!")
