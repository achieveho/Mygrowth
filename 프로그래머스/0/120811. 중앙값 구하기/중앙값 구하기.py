def solution(array):
    new_array = sorted(array, reverse = True)
    return new_array[len(new_array) // 2]