def solution01(a, b):
    return a * a + b * b if a & b & 1 else (a + b) << 1 if (a | b) & 1 else abs(a - b)