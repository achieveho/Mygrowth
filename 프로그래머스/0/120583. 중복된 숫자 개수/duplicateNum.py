def solution01(array, n):
    return array.count(n)

def solution02(array, n):
    cnt = 0
    for i in array:
        if i == n:
            cnt += 1
    
    return cnt