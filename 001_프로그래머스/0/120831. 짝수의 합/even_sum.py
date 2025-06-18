def solution(n):
    return sum(range(2, n + 1, 2))

def solution2(n):
    return 2 * (n // 2) * ((n // 2) + 1) / 2