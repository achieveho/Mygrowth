def solution01(hp):
    return (hp // 5) + (hp % 5 // 3) + ((hp % 5) % 3)

def solution02(hp):
    answer = 0
    for ant in [5, 3, 1]:
        d, hp = divmod(hp, ant)
        answer += d
    
    return answer