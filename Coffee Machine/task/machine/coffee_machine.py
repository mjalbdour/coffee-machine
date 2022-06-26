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
MSG_CAN_MAKE = "Yes, I can make that amount of coffee"
MSG_CAN_MAKE_MORE_1 = "Yes, I can make that amount of coffee (and even"
MSG_CAN_MAKE_MORE_2 = "more than that)"
MSG_CANNOT_MAKE_1 = "No, I can make only"
MSG_CANNOT_MAKE_2 = "cups of coffee"

print(MSG_INTAKE_WATER)
intake_water = int(input())

print(MSG_INTAKE_MILK)
intake_milk = int(input())

print(MSG_INTAKE_COFFEE_BEANS)
intake_coffee_beans = int(input())

print(MSG_NUMBER_OF_CUPS)
cups = int(input())

produced_cups = min(intake_water // 200, intake_milk // 50, intake_coffee_beans // 15)

result = produced_cups - cups

if result == 0:
    print(f'{MSG_CAN_MAKE}')
elif result > 0:
    print(f'{MSG_CAN_MAKE_MORE_1} {result} {MSG_CAN_MAKE_MORE_2}')
elif result < 0:
    print(f'{MSG_CANNOT_MAKE_1} {produced_cups} {MSG_CANNOT_MAKE_2}')
