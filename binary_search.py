

def binary_search(number_list: list, number: int) -> int:
    """
    Perform a binary search of a list of integers and return index of target
    """
    number_list.sort()

    start, end = 0, (len(number_list)-1)

    while start <= end:
        midpoint = (start + end) // 2
        if number == number_list[midpoint]:
            return midpoint
        elif number > number_list[midpoint]:
            start = midpoint + 1
        elif number < number_list[midpoint]:
            end = midpoint - 1

    return -1


def main():
    number_list = [2, 4, 6, 8, 7, 10, 13, 17, 23, 22, 12, 3, 5, 32]

    x = int(input('Target number: '))
    index = binary_search(number_list, x)
    if index > 0:
        print(sorted(number_list))
        print(f"Index of number {number_list[index]} -> {index}")
    else:
        print(f'Number ({x}) not found in list')


if __name__ == "__main__":
    main()
