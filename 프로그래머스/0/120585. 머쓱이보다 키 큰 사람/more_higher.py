def solution01(array, height):
    return sum(1 for a in array if a > height)

def solution02(array, height):
    return sum(h > height for h in array)