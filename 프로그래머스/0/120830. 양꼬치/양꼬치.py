def solution(n, k):
    if (0 < n < 1000) and (int(n /10) <= k < 1000):
        if n // 10 >= 1:
            free = (n // 10)
            return ((n * 12000) + (k * 2000) - (free * 2000))
        return (n * 12000) + (k * 2000)