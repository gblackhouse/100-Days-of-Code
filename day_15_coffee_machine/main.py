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

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

making_coffee= True

while making_coffee:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        making_coffee = False
    elif choice == "report":
        print("Water:", resources["water"], "ml")
        print("Milk:", resources["milk"], "ml")
        print("Coffee:", resources["coffee"], "g")
        print("Money: $", money)
    elif choice in MENU:
        drink = MENU[choice]
        required_ingredients = drink["ingredients"]
        cost = drink["cost"]

        can_make = True
        for item in required_ingredients:
            if required_ingredients[item] > resources.get(item, 0):
                print("Sorry there is not enough", item + ".")
                can_make = False

        if can_make:
            print("Insert coins.")
            quarters = int(input("How many quarters?: ")) * 0.25
            dimes = int(input("How many dimes?: ")) * 0.10
            nickels = int(input("How many nickels?: ")) * 0.05
            pennies = int(input("How many pennies?: ")) * 0.01

            total_inserted = quarters + dimes + nickels + pennies

            if total_inserted >= cost:
                change = round(total_inserted - cost, 2)
                if change > 0:
                    print(f"Here is $", change, "in change.")
                money += cost

                for item in required_ingredients:
                    resources[item] -= required_ingredients[item]

                print(f"Here is your", choice,"☕ Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
