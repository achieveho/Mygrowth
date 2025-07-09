def solution(number):
    result = 0
    for i in range(len(number)):
        result += int(number[i])
    
    return result % 9