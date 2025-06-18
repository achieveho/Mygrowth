def solution(n):
    if (0 < n <= 1000):
        result = 0
        for i in range(0, n + 1, 2):
            result += i
        return result