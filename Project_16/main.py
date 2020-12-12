def User_Input():
    return int(input("Input a year: "))


def Process(input):
    if input % 4 == 0:
        if input % 100 == 0:
            if input % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def main():
    user_input = User_Input()
    result = Process(user_input)
    print("Is Leap Year") if result == 1 else print("Is Not Leap Year")


if __name__ == '__main__':
    main()
