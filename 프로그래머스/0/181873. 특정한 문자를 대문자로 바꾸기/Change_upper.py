def solution01(my_string, alp):
    return my_string.replace(alp, alp.upper())


def solution02(my_string, alp):
    return ''.join([i.upper() if i == alp else i for i in my_string])