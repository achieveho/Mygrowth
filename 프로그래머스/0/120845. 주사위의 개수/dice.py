def solution01(box, n):
    x, y, z = box
    return (x // n) * (y // n) * (z // n)

def solution02(box, n):
    answer = 1
    for b in box:
        answer *= b // n
    
    return answer

import math

def solution03(box, n):
    return math.prod(map(lambda v: v // n, box))