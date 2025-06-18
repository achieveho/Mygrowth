def solution(n):
    if (1 <= n <= 1000000):
        r = n ** 0.5
        if r == int(r):
            return 1
        return 2
    return