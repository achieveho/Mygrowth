def solution01(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2