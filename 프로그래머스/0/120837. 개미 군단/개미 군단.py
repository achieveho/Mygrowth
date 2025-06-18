def solution(hp):
    top = hp // 5
    mid = (hp % 5) // 3
    bot = ((hp % 5) % 3) // 1
    return top + mid + bot