import random
numbers = [7, 47, 51, 69, 78, 99, 107, 451, 999]


def binary_search(arr):
    length = len(arr)

    low = 1
    high = length

    print(length)

    target = random.choice([7, 47, 51, 69, 78, 99, 107, 451, 999])
    print("Target is ", target)

    midpoint = int(length / 2)

    while numbers[midpoint] != target:
        # print(midpoint)
        midpoint = int(length/2)
        print("Midpoint is  ", midpoint)
        if numbers[midpoint] == target:
            print("Your number is found at index number ",
                  midpoint, " and the value is ", numbers[midpoint])
        elif numbers[midpoint] > target:
            high = midpoint
            length = high
        elif numbers[midpoint] < target:
            low = midpoint
            length = high + low


binary_search(numbers)
