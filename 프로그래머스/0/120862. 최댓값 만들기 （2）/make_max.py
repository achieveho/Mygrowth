def solution01(numbers):
    numbers = sorted(numbers)

    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])

def solution02(numbers):
    numbers.sort()

    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])