def solution01(myString):
    return [len(w) for w in myString.split('x')]


def solution02(myString):
    ans = []
    cnt = 0
    for s in myString:
        if s != 'x':
            cnt += 1
        else:
            ans.append(cnt)
            cnt = 0
    ans.append(cnt)

    return ans


def solution03(myString):
    return list(map(lambda x: len(x), myString.split('x')))