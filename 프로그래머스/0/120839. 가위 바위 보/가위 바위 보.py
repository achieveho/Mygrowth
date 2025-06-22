def solution(rsp):
    result = ""
    for i in range(0, len(rsp)):
        if rsp[i] == '2':
            result += '0'
        elif rsp[i] == '0':
            result += '5'
        elif rsp[i] == '5':
            result += '2'
        else:
            return
    
    return result