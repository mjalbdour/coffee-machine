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

cups = int(input())
water = 200 * cups
milk = 50 * cups
coffee_beans = 15 * cups
print(f'{MSG_RESULT_1} {cups} {MSG_RESULT_2}')
print(f'{water} {MSG_WATER}')
print(f'{milk} {MSG_MILK}')
print(f'{coffee_beans} {MSG_COFFEE_BEANS}')
