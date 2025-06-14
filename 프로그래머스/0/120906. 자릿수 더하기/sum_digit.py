def solution01(n):
    return sum(int(i) for i in str(n))

def solution02(n):
    answer = 0
    while n:
        answer += n % 10
        n //= 10
    return answer

def solution03(n):
    answer = 0
    while n:
        n, r = divmod(n, 10)
        answer += r
    return answer