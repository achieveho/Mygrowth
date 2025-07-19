def solution(num_list):
    sum1 = sum(num_list[0::2])
    sum2 = sum(num_list[1::2])
    if sum1 > sum2:
        return sum1
    elif sum1 < sum2:
        return sum2
    return sum1