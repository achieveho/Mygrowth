def solution01(slice, n):
    return ((n - 1) // slice) + 1

def solution02(slice, n):
    d, m = divmod(n, slice)
    return d + int(m != 0)          # 'm = 0'이면 0, 'm != 0'이면 1 반환.

from math import ceil
def solution(slice, n):
    return ceil(n/slice)