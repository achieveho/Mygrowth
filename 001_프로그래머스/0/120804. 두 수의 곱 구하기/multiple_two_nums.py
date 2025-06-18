def solution(num1, num2):
    i = 0
    answer = 0
    
    while i < num2:
        answer += num1
        i += 1
    
    return answer

# print(solution(10, 20))