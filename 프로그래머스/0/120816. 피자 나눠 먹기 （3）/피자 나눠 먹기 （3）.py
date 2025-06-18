def solution(slice, n):
    s, r = divmod(n, slice)
    if not r == 0:
        s += 1
    return s