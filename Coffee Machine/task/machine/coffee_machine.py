#
# output = """Starting to make a coffee
# Grinding coffee beans
# Boiling water
# Mixing boiled water with crushed coffee beans
# Pouring coffee into the cup
# Pouring some milk into the cup
# Coffee is ready!"""
#
# print(output)

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
MSG_BUY = "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: "
MSG_TAKE_MONEY = "I gave you $"
MSG_MACHINE_HAS = "The coffee machine has:"
MSG_DISPOSABLE_CUPS = "disposable cups"
MSG_MONEY = "of money"
MSG_ACTION = "Write action (buy, fill, take):"


class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550

    def buy_1(self):
        self.water -= 250
        self.coffee_beans -= 16
        self.money += 4

    def buy_2(self):
        self.water -= 350
        self.milk -= 75
        self.coffee_beans -= 20
        self.money += 7

    def buy_3(self):
        self.water -= 200
        self.milk -= 100
        self.coffee_beans -= 12
        self.money += 6

    def buy(self):
        print(MSG_BUY)
        option = input()
        self.options_buy[option](self)
        self.cups -= 1

    def take(self):
        print(f'{MSG_TAKE_MONEY}{self.money}')
        self.money = 0

    def fill(self):
        print(MSG_INTAKE_WATER)
        self.water += int(input())

        print(MSG_INTAKE_MILK)
        self.milk += int(input())

        print(MSG_INTAKE_COFFEE_BEANS)
        self.coffee_beans += int(input())

        print(MSG_INTAKE_CUPS)
        self.cups += int(input())

    def print_state(self):
        print(f'\n{MSG_MACHINE_HAS}')
        print(f'{self.water} {MSG_WATER}')
        print(f'{self.milk} {MSG_MILK}')
        print(f'{self.coffee_beans} {MSG_COFFEE_BEANS}')
        print(f'{self.cups} {MSG_DISPOSABLE_CUPS}')
        print(f'${self.money} {MSG_MONEY}')

    def handle_option(self):
        self.print_state()
        print(MSG_ACTION)
        option = input()
        self.options[option](self)
        self.print_state()

    options = {
        "buy": buy,
        "fill": fill,
        "take": take
    }

    options_buy = {
        "1": buy_1,
        "2": buy_2,
        "3": buy_3
    }


# print(MSG_INTAKE_WATER)
# intake_water = int(input())
#
# print(MSG_INTAKE_MILK)
# intake_milk = int(input())
#
# print(MSG_INTAKE_COFFEE_BEANS)
# intake_coffee_beans = int(input())
#
# print(MSG_NUMBER_OF_CUPS)
# cups = int(input())
#
# produced_cups = min(intake_water // 200, intake_milk // 50, intake_coffee_beans // 15)
#
# result = produced_cups - cups
#
# if result == 0:
#     print(f'{MSG_CAN_MAKE}')
# elif result > 0:
#     print(f'{MSG_CAN_MAKE_MORE_1} {result} {MSG_CAN_MAKE_MORE_2}')
# elif result < 0:
#     print(f'{MSG_CANNOT_MAKE_1} {produced_cups} {MSG_CANNOT_MAKE_2}')


# def main():
#     coffee_machine = CoffeeMachine()
#     coffee_machine.handle_option()

coffee_machine = CoffeeMachine()
coffee_machine.handle_option()


# if __name__ == "main":
#     main()
