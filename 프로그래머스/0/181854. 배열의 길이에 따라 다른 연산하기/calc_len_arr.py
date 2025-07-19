def solution01(arr, n):
    l = len(arr)
    if n % 2:
        for i in range(0, n, 2):
            arr[i] += n
    else:
        for i in range(1, n, 2):
            arr[i] += n
    
    return arr


def solution02():
    lambda a, n: [x + n if i % 2 == (len(a) + 1) % 2 else x for i, x in enumerate(a)]


def solution03(arr, n):
    ans = []
    k = len(arr) % 2
    for i, a in enumerate(arr):
        if (i + k) % 2 != 0:
            ans.append(a + n)
        else:
            ans.append(a)
    
    return ans