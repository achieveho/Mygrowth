def solution01(n):
    return [i for i in range(1, n + 1, 2)]

def solution02(n):
    return [x for x in range(n + 1) if x % 2]

def solution03(n):
    return list(range(1, n + 1, 2))

def solution04(n):
    answer = list(filter(lambda x: x % 2, range(n + 1)))
    return answer