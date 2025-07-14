def solution(num, k):
    num, k = str(num), str(k)
    if num.find(k) != -1:
        return num.find(k) + 1
    else:
        return -1