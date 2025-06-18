def solution01(dot):
    quad = [(3, 2), (1, 4)]
    return quad[dot[0] > 0][dot[1] > 0]

def solution02(dot):
    x, y = dot
    if x * y > 0:
        return 1 if x > 0 else 3
    else:
        return 4 if x > 0 else 2

def solution03(dot):
    a, b = 1, 0
    if dot[0] * dot[1] > 0:
        b = 1
    if dot[1] < 0:
        a = 2
    return 2 * a - b

def solution04(dot):
    return [[1, 4], [2, 3]][dot[0] < 0][dot[1] < 0]