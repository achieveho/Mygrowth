def solution(num_list):
    result = [0, 0]
    
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            result[0] += 1
        else:
            result[1] += 1
    
    return result