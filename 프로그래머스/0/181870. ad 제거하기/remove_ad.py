def solution01(strArr):
    return [word for word in strArr if 'ad' not in word]


def solution02(strArr):
    answer = []
    for x in strArr:
        if 'ad' in x:
            continue
        answer.append(x)
    
    return answer


def solution03(strArr):
    for str in strArr[:]:
        if 'ad' in str:
            strArr.remove(str)
    
    return strArr


def solution04(strArr):
    return [str for str in strArr if str.find('ad') == -1]


def solution05(strArr):
    return list(filter(lambda x: 'ad' not in x, strArr))