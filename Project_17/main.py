def checkfibonacci(n):
    a = 0
    b = 1
    if n == a or n == b:
        return True
    c = a+b
    while(c <= n):
        if(c == n):
            return True
        a = b
        b = c
        c = a + b
    return False


def main():
    print(checkfibonacci(int(input())))


if __name__ == '__main__':
    main()
