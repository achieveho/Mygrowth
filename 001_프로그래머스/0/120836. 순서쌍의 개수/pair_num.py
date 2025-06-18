def solution01(n):
    answer = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            answer += 2
            if i * i == n:
                answer -= 1
    
    return answer

def solution02(n):
    return len(list(filter(lambda v: n % (v + 1) == 0, range(n))))

def solution03(n):
    return len([number for number in range(1, n + 1) if n % number == 0])
