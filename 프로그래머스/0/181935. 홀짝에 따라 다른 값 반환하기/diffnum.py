def solution01(n):
    if n % 2:
        return sum(range(1, n+1, 2))
    return sum([i*i for i in range(2, n+1, 2)])


def solution02(n):
    return sum(x ** (2 - x % 2) for x in range(n + 1) if n % 2 == x % 2)


def solution03(n):
    answer = 0
    if n % 2:
        for i in range(1, n + 1, 2):
            answer += i
    else:
        for i in range(2, n + 1, 2):
            answer += i ** 2
    
    return answer