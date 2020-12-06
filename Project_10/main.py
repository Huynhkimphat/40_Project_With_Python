import random


def create_list(n):
    samples = (random.sample(range(0, 100), n))
    return sorted(samples)


def process(bot_list):
    your_choice = int(input())
    if binary_search(bot_list, 0, len(bot_list)-1, your_choice) == -1:
        return"Do Not Have Your Number"
    return "YES"


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


def main():
    choice = int(input())
    bot_list = create_list(choice)
    print(bot_list)
    print(process(bot_list))


if __name__ == "__main__":
    main()
