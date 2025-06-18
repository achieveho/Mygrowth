def solution(s1, s2):
    cnt = 0
    if len(s1) >= len(s2):
        for i in range(len(s2)):
            if s2[i] in s1:
                cnt += 1
            continue
    else:
        for i in range(len(s1)):
            if s1[i] in s2:
                cnt += 1
            continue
    
    return cnt