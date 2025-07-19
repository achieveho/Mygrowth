def solution(arr1, arr2):
    if len(arr1) == len(arr2):
        sum1, sum2 = sum(arr1), sum(arr2)
        if sum1 > sum2:
            return 1
        elif sum2 > sum1:
            return -1
        else:
            return 0
    else:
        if len(arr1) > len(arr2):
            return 1
        else:
            return -1