def solution(num_list):
    result = 1
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        for i in num_list:
            result *= i
        return result