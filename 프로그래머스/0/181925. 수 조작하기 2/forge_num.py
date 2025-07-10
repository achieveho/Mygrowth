def solution01(log):
    res = ''
    joystick = dict(zip([1, -1, 10, -10], ['w', 's', 'd', 'a']))
    for i in range(1, len(log)):
        res += joystick[log[i] - log[i - 1]]
    
    return res


def solution02(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i - 1]    # 현재 값과 이전 값의 차이 계산
        if diff == 1:
            answer += 'w'
        elif diff == -1:
            answer += 's'
        elif diff == 10:
            answer += 'd'
        elif diff == -10:
            answer += 'a'
    
    return answer


def solution03(numLog):
    d = {'1':'w', '-1':'s', '10':'d', '10':'a'}
    answer = ''
    for i in range(1, len(numLog)):
        answer += d[str(numLog[i] - numLog[i - 1])]
    
    return answer