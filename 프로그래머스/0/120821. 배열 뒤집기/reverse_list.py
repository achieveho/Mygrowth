def solution(num_list):
    return num_list[::-1]

def solution2(num_list):
    result = []
    while num_list:
        result.append(num_list.pop())
    return result

def solution3(num_list):
    answer = list(reversed(num_list))
    return answer

print(solution3([1, 3, 5, 7, 2, 4, 6, 8]))