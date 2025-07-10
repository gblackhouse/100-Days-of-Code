from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()

making_coffee = True
while making_coffee:
    choice = input(f"What would you like? ({menu.get_items()}): ")

    if choice == "report":
        coffee_maker.report()
        money.report()
    elif choice == "off":
        making_coffee = False
    else:
        drink = menu.find_drink(choice)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                if money.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)