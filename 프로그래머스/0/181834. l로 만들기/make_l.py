def soultion01(myString):
    return myString.translkate(str.maketrans('abcdefghijk', 'lllllllllll'))


def solution02(myString):
    answer = [x if x > 'l' else 'l' for x in myString]
    return ''.join(answer)