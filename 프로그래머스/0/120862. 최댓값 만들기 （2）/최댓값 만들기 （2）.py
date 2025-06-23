def solution(numbers):
    de_numbers = sorted(numbers, reverse = True)
    if (de_numbers[0] * de_numbers[1]) >= (de_numbers[-1] * de_numbers[-2]):
        return (de_numbers[0] * de_numbers[1])
    else:
        return (de_numbers[-1] * de_numbers[-2])