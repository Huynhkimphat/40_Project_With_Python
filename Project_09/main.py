def Your_Input():
    return str(input()).strip()


def Process(your_input):
    username = your_input[:your_input.index("@")]
    domain_name = your_input[your_input.index("@")+1:]
    return [username, domain_name]


def main():
    print("Start")
    your_input = Your_Input()
    result = Process(your_input)
    print("Username: {} \nDomain name: {}".format(result[0], result[1]))


if __name__ == "__main__":
    main()
