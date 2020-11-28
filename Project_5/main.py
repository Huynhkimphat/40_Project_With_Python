import random


def game_number():
    print("How many game do you want to play")
    game = eval(input())
    return game


def menu():
    print("Choose Rock-Paper-Scissors")
    print("1.Rock   2.Paper 3.Scissors")


def process_game(bot_choice, your_choice):
    # 0:draw/tie
    # 1:you win bot lose
    # -1:you lose bot win
    if bot_choice == your_choice:
        return 0  # tie
    if bot_choice == 1:
        if your_choice == 2:
            return 1  # you win
        if your_choice == 3:
            return -1  # you lose
    if bot_choice == 2:
        if your_choice == 1:
            return -1
        if your_choice == 3:
            return 1
    if bot_choice == 3:
        if your_choice == 1:
            return -1
        if your_choice == 2:
            return -1


def yourChoice():
    choice = 0
    while choice != 1 and choice != 2 and choice != 3:
        print("Enter your choice: ")
        choice = eval(input())
    return choice


def botChoice():
    choice = random.randrange(1, 4)
    return choice


def print_choice(yourChoice, botChoice):
    if yourChoice == 1:
        you = "Rock"
    elif yourChoice == 2:
        you = "Paper"
    else:
        you = "Scissors"
    if bot_choice == 1:
        bot = "Rock"
    elif bot_choice == 2:
        bot = "Paper"
    else:
        bot = "Scissors"
    print("YOU: " + you + " BOT: " + bot)


def status(result, you, bot, draw):
    if result == 1:
        return [you+1, bot, draw]
    elif result == -1:
        return [you, bot+1, draw]
    return [you, bot, draw+1]


def after1game(you, bot, tie):
    print("YOU: " + str(you)+" BOT: " + str(bot)+" TIE: " + str(tie))


def to_sum_up(you, bot):
    if you > bot:
        return "YOU WIN"
    elif you == bot:
        return "TIE"
    return "YOU LOSE"


number_game = game_number()
you_win = 0
bot_win = 0
draw = 0
while number_game != 0:
    menu()
    your_choice = yourChoice()
    bot_choice = botChoice()
    print_choice(your_choice, bot_choice)
    result = process_game(bot_choice, your_choice)
    [you_win, bot_win, draw] = status(result, you_win, bot_win, draw)
    after1game(you_win, bot_win, draw)
    number_game -= 1
print(to_sum_up(you_win, bot_win))
