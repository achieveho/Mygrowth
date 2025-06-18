def solution(array, n):
    cnt = 0
    for i in range(len(array)):
        if n == array[i]:
            cnt += 1
    return cnt