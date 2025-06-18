def solution(num_list):
    result = [0, 0]

    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            result[0] += 1
        else:
            result[1] += 1
    
    return result

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

def solution2(num_list):
    result = [0, 0]

    for i in num_list:
        result[i % 2] += 1

    return result

def solution3(num_list):
    odd = sum(1 for n in num_list if n % 2)
    