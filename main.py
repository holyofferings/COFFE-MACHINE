from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# creating object of MoneyMachine class
money_machine = MoneyMachine()
# Creating object of Coffee Maker class
coffee_maker = CoffeeMaker()
# Creating object of menu class
menu = Menu()
# Loop to run the coffee machine
is_on = True
while is_on:
    # Displays the items in the menu class
    options = menu.get_items()
    choice = input(f"What would you like to have{options}: ")
    if choice == "off":
        print("Thanks for coming by. See u later.")
        is_on = False
    elif choice == "report":
        # Reports the ingredients left and the money left in the machine with the help of the money_machine
        # and coffee_maker objects
        coffee_maker.report()
        money_machine.report()
    else:
        # Choosing the drink from the menu items class object.
        drink = menu.find_drink(choice)
        # Checking for the Sufficient resources.
        # Processing the money as per the cost of each drink.

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

