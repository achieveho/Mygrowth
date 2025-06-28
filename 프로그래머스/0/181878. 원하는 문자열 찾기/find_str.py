def solution01(myString, pat):
    return int(pat.lower() in myString.lower())

def solution02(myString, pat):
    return min(1, myString.lower().find(pat.lower()) + 1)