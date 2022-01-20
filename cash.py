import importlib
from cs50 import get_float


# prompt user for change owed
while True:
    try:
        dollar = get_float("change owed: ")
        if dollar > 0:
            break
    except ValueError:
        print("Enter a valid value")
# converting the user’s inputted dollars to cents
cents = round(int(dollar * 100))
coins = 0
while cents > 0:
    if cents >= 25:
        coins += 1
        cents -= 25
    elif cents >= 10:
        coins += 1
        cents -= 10
    elif cents >= 5:
        coins += 1
        cents -= 5
    elif cents >= 1:
        coins += 1
        cents -= 1
print(coins)


def user_input():
    while True:
        try:
            n = get_float("change owed: ")
            if n > 0:
                break
        except ValueError:
            print("Enter a valid value")
    count = 0
    while cents > 0:
        if cents >= 25:
            count += 1
            cents -= 25
        elif cents >= 10:
            count += 1
            cents -= 10
        elif cents >= 5:
            count += 1
            cents -= 5
        elif cents >= 1:
            count += 1
            cents -= 1


