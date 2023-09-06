# This is a sample Python script.
from random import randint  # will give us access to random numbers - this is built-in to Python


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fridge = {
        "milk": 5,
        "bananas": 4,
        "juice": 2,
    }

    if fridge["milk"] == 1:
        print("There is one bottle of milk left")
    else:
        print("There are " + str(fridge["milk"]) + " bottles of milk left")

    nums = [2, 4, 6]




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
