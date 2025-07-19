def solution01():
    return lambda x: x.split()


def solution02(myString):
    return [i for i in myString.split(" ") if i != ""]


import re
def solution03(myString):
    return re.findall(r"[a-z]+", myString)