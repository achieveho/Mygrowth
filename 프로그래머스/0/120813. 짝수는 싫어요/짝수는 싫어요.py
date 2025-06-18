def solution(n):
    result = []
    for i in range(1, n + 1, 2):
        result.append(i)
    result.sort()
    
    return result