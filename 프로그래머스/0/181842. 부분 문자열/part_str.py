def solution01(str1, str2):
    return int(str1 in str2)


def solution02(str1, str2):
    return 1 if str1 in str2 else 0


def solution03(str1, str2):
    return [0, 1][str1 in str2]