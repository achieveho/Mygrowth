def solution01(n):
    answer = [[0] * n for i in range(n)]
    for i in range(n):
        answer [i][i] = 1
    
    return answer

import numpy as np

def solution02(n):
    return np.eye(n).tolist()


def solution03(n):
    result = []
    for i in range(n):
        arr = [0] * n
        arr[i] = 1
        result.append(arr)
    
    return result