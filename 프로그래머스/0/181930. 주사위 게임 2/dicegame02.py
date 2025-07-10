def solution(a, b, c):
    check = len(set([a, b, c]))
    if check == 1:
        return 3 * a * 3 *(a ** 2) * 3 * (a ** 3)
    elif check == 2:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    else:
        return (a + b + c)
    

def solution02(a, b, c):
    list = [a, b, c]
    answer = 1
    for i in range(4 - len(set(list))):
        answer *= a ** (i + 1) + b ** (i + 1) + c ** (i + 1)
    
    return answer