def solution01(my_string, target):
    return int(target in my_string)


def solution02():
    return lambda x, y: int(x, y)


def solution03(my_string, target):
    return 1 if my_string.find(target) >= 0 else 0