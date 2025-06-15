def solution01(s1, s2):
    return len(set(s1) & set(s2))

def solution02(s1, s2):
    answer = 0

    for word in s1:
        if word in s2:
            answer += 1
        else:
            continue
    
    return answer

def solution03(s1, s2):
    dic = {i: 1 for i in s1}
    answer = sum(dic.get(j, 0) for j in s2)
    return answer

def solution04(s1, s2):
    count = 0
    for val in s1:
        if val in s2:
            count += 1
    return count