import random

bot_result = random.randint(0, 100)


def game_start():
    your_choice = int(input())
    if your_choice < bot_result:
        print("Your choice is smaller than result!!!")
        return 0
    if your_choice > bot_result:
        print("Your choice is higher than result!!!")
        return 0
    print("Bingo!!!")
    return 1


if __name__ == "__main__":
    your_score = 10
    while(game_start() == 0 and your_score != 0):
        your_score -= 1
    if your_score != 0:
        print("YOUR SCORE: " + str(your_score))
    else:
        print("You lose the game \nThe answer is " + str(bot_result))
