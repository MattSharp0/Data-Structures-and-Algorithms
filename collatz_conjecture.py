import sys

# if even, divide by 2. If off, multiply by 3 and add 1


def collatz(n):
    print(n, end='', flush=True)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(f', {n}', end='', flush=True)
    print('')


def main():
    n = int(input('Provide starting number -> '))
    if n >= 1:
        collatz(n)
    else:
        print('Number must be greater than 0')
        sys.exit()


if __name__ == "__main__":
    main()
