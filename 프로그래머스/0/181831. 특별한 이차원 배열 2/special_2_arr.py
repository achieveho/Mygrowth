def solution01(arr):
    return int(arr == list(map(list, zip(*arr))))


def solution02(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0
    
    return 1