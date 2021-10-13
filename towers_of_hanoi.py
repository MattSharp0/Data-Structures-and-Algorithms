# Solve for f(1)
# Assume f(n-1)
# Show f(n) using f(n-1)


def towers_of_hanoi(n: int, start: int, end: int):

    def print_move(start, end):
        print(f'{start} -> {end}')

    if n == 1:
        print_move(start, end)

    else:
        other = (6 - (start + end))
        towers_of_hanoi(n=(n-1), start=start, end=other)
        print_move(start, end)
        towers_of_hanoi(n=(n-1), start=other, end=end)


discs = int(input('Number of discs [must be 1 or more] -> '))
assert discs >= 1
start = int(input('Starting pole [1, 2 or 3] -> '))
assert start >= 1 and start <= 3
end = int(input(f'Ending pole [As above, cannot be {start}] -> '))
assert end >= 1 and end <= 3 and start != end

towers_of_hanoi(discs, start, end)

# towers_of_hanoi(3, 1, 3)
# 1 -> 3
# 1 -> 2
# 3 -> 2
# 1 -> 3
# 2 -> 1
# 2 -> 3
# 1 -> 3
