def solution01(my_string, n):
    return ''.join(i * n for i in my_string)

def solution02(my_string, n):
    answer = ''
    for m in my_string:
        answer += m * n
    
    return answer