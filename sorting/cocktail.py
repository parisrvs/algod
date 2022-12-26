import random


def cocktail(numbers: list[int]) -> list[int]:
    len_numbers = len(numbers)
    swapped = True
    start = 0
    end = len_numbers - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

        if not swapped:
            break

        end -= 1
        swapped = False

        for i in range(end - 1, start - 1, -1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

        start += 1

    return numbers


if __name__ == '__main__':
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(nums)
    print(cocktail(nums))



