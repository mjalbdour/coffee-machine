
from sys import exit

MSG_NUMBER_OF_CUPS = "Write how many cups of coffee you will need:"
MSG_RESULT_1 = "For"
MSG_RESULT_2 = "cups of coffee you will need:"
MSG_WATER = "ml of water"
MSG_MILK = "ml of milk"
MSG_COFFEE_BEANS = "g of coffee beans"
MSG_INTAKE_WATER = "Write how many ml of water the coffee machine has:"
MSG_INTAKE_MILK = "Write how many ml of milk the coffee machine has:"
MSG_INTAKE_COFFEE_BEANS = "Write how many grams of coffee beans the coffee machine has:"
MSG_INTAKE_CUPS = "Write how many disposable cups you want to add:"
MSG_CAN_MAKE = "Yes, I can make that amount of coffee"
MSG_CAN_MAKE_MORE_1 = "Yes, I can make that amount of coffee (and even"
MSG_CAN_MAKE_MORE_2 = "more than that)"
MSG_CANNOT_MAKE_1 = "No, I can make only"
MSG_CANNOT_MAKE_2 = "cups of coffee"
MSG_BUY = "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"
MSG_TAKE_MONEY = "I gave you $"
MSG_MACHINE_HAS = "The coffee machine has:"
MSG_DISPOSABLE_CUPS = "disposable cups"
MSG_MONEY = "of money"
MSG_ACTION = "Write action (buy, fill, take, remaining, exit):"
MSG_MAKING_COFFEE = "I have enough resources, making you a coffee!"
MSG_NOT_ENOUGH = "Sorry, not enough"


class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550

    def buy_item(self, item):
        if self.water - item["water"] < 0:
            print(f'{MSG_NOT_ENOUGH} water!')
        elif self.milk - item["milk"] < 0:
            print(f'{MSG_NOT_ENOUGH} milk!')
        elif self.coffee_beans - item["coffee_beans"] < 0:
            print(f'{MSG_NOT_ENOUGH} coffee beans!')
        elif self.cups < 1:
            print(f'{MSG_NOT_ENOUGH} cups!')
        else:
            self.water -= item["water"]
            self.milk -= item["milk"]
            self.coffee_beans -= item["coffee_beans"]
            self.money += item["money"]
            self.cups -= 1
            print(MSG_MAKING_COFFEE)

    def buy(self):
        print(f'\n{MSG_BUY}')
        option = input()
        if option == "back":
            return
        self.buy_item(self.options_buy[option])

    def fill(self):
        print(MSG_INTAKE_WATER)
        self.water += int(input())

        print(MSG_INTAKE_MILK)
        self.milk += int(input())

        print(MSG_INTAKE_COFFEE_BEANS)
        self.coffee_beans += int(input())

        print(MSG_INTAKE_CUPS)
        self.cups += int(input())

    def remaining(self):
        print(f'\n{MSG_MACHINE_HAS}')
        print(f'{self.water} {MSG_WATER}')
        print(f'{self.milk} {MSG_MILK}')
        print(f'{self.coffee_beans} {MSG_COFFEE_BEANS}')
        print(f'{self.cups} {MSG_DISPOSABLE_CUPS}')
        print(f'${self.money} {MSG_MONEY}')

    def take(self):
        print(f'{MSG_TAKE_MONEY}{self.money}')
        self.money = 0

    def handle_option(self):
        print(f'\n{MSG_ACTION}')
        option = input()
        self.options[option](self)

    options = {
        "buy": buy,
        "fill": fill,
        "take": take,
        "remaining": remaining,
        "exit": exit
    }

    options_buy = {
        "1": {"water": 250, "milk": 0, "coffee_beans": 16, "money": 4},
        "2": {"water": 350, "milk": 75, "coffee_beans": 20, "money": 7},
        "3": {"water": 200, "milk": 100, "coffee_beans": 12, "money": 6},
    }


coffee_machine = CoffeeMachine()
while True:
    coffee_machine.handle_option()
