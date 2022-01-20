# a program that prints out a half-pyramid of a specified height

import importlib


def main():
    height = get_height()
    # printing hash as like right alighned pyramid
    for i in range(height):
        for j in range(height):
            if j < (height-(i+1)):
                print(" ", end="")
            else:
                print("#", end="")
        print()


def get_height():
    # prompt the user for height untill the given condition is met
    while True:
        try:
            n = int(input("Height: "))
            if n > 0 and n <= 8:
                break
        except ValueError:
            print("That's not an integer!")
    return n


main()
