def solution(num_list):
    result = 0
    if num_list[-1] > num_list[-2]:
        result = num_list[-1] - num_list[-2]
        num_list.append(result)
    else:
        result = num_list[-1] * 2
        num_list.append(result)
        
    return num_list