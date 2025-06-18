def solution01(a, b):
    return int(max(f"{a}{b}", f"{a}{b}"))

def solution02(a, b):
    return max(int(str(a) + str(b)), int(str(b) + str(a)))