def solution01(myString, pat):
    myString = myString.replace('A', 'a').replace('B', 'A').replace('a', 'B')
    
    if pat in myString:
        return 1
    return 0


def solution02(myString, pat):
    return int(''.join(['A' if i == 'B' else 'B' for i in pat]) in myString)


def solution03(myString, pat):
    return int(pat in ''.join('AB'[ch == 'A'] for ch in myString))