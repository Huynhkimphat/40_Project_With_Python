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
    return(game(choose))


print(main())
