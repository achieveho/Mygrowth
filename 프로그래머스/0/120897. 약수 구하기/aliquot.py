def solution01(n):
    answer = [i for i in range(1, n + 1) if n % i == 0]

    return answer

def solution02(n):
    return list(filter(lambda v: n % v == 0, [i for i in range(1, n // 2 + 1)])) + [n]