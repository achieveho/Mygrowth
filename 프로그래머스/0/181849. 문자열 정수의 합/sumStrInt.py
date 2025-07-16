def solution01(num_str):
    return sum(map(int, num_str))


def solution02():
    return lambda x: sum(map(int, x))


def solution03(num_str):
    return sum([int(i) for i in num_str])