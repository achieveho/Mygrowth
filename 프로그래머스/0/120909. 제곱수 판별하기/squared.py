def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2

def solution1(n):
    return 1 if (n ** 0.5) % 1 == 0 else 2