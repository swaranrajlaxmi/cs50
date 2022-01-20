import importlib


def main():
    height = get_height()
    # printing hash as like both right and left alighned pyramid
    for i in range(1, height + 1):
        # print spaces and hashes
        print(" " * (height - i) + "#" * i, end="")
        # print 2 spaces
        print(" " * 2, end="")
        # print right hashes
        print("#" * i, end="")
        print()


def get_height():
    # prompt the user for height untill the given condition is met
    while True:
        try:
            n = int(input("Height: "))
            if n > 0 and n < 9:
                break
            print("Invalid")
        except ValueError:
            print("That's not an integer")
    return n


main()