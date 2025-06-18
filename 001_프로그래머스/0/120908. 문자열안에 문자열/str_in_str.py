def solution01(str1, str2):
    return 1 if str2 in str1 else 2

def solution02(str1, str2):
    return 1 + int(str2 not in str1)

def solution03(str1, str2):
    if str1.count(str2):
        return 1
    else:
        return 2

def solution04(str1, str2):
    answer = str1.split(str2)
    if len(answer) == 1:
        return 2
    else:
        return 1

def solution05(str1, str2):
    return 1 if str1.find(str2) >= 0 else 2

def solution06(str1, str2):
    return 2 - (str2 in str1)