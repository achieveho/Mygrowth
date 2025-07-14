def solution01(num, k):
    return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1


def solution02(num, k):
    for i, n in enumerate(str(num)):
        if str(k) == n:
            return i + 1
    return -1


def solution03(num, k):
    try:
        return str(num).index(str(k)) + 1
    except ValueError:
        return -1