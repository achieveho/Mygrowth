def solution01(arr, k):
    return [i * k if k % 2 != 0 else i + k for i in arr]


def solution02(arr, k):
    if k % 2 != 0:
        return list(map(lambda x: x * k, arr))
    else:
        return list(map(lambda x: x + k, arr))
    

def solution03(arr, k):
    return [i * k if k & 1 else i + k for i in arr]