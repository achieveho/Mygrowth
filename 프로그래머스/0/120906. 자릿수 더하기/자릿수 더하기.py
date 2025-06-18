def solution(n):
    result = 0
    sepa = list(map(int, str(n)))
    for i in sepa:
        result += i
    
    return result