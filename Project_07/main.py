import random


def menu():
    print("Press: ")
    print("1. Start Game")
    print("0.Exit Game")


def choice():
    return eval(input())


def game(choose):
    if choose == 1:
        return random.randrange(1, 7)
    return


def main():
    menu()
    choose = choice()
    while choose == 1:
        print(random.randrange(1, 7))
        print("Do you want to play again?\n(1/0)")
        choose = choice()
    else:
        return "Thanks you"


if __name__ == "__main__":
    print(main())
