def solution(n):
    cnt = 0
    for i in range(n + 1):
        if n % (i + 1) == 0:
            cnt += 1
        continue
    
    return cnt