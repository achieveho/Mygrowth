def solution01(arr1, arr2):
    return (len(arr1) > len(arr2)) - (len(arr2) > len(arr1)) or (sum(arr1) - sum(arr2)) - (sum(arr2) > sum(arr1))


def solution02(arr1, arr2):
    if len(arr1) < len(arr2):
        return -1
    elif len(arr1) > len(arr2):
        return 1
    elif sum(arr1) < sum(arr2):
        return -1
    elif sum(arr1) > sum(arr2):
        return 1
    else:
        return 0


def solution03(arr1, arr2):
    if len(arr1) > len(arr2) or sum(arr1) > sum(arr2):
        return 1
    elif len(arr1) < len(arr2) or sum(arr1) < sum(arr2):
        return -1
    else:
        return 0
    

def solution04(arr1, arr2):
    return int(bool((len(arr1)-len(arr2))/abs(len(arr1)-len(arr2))+1))*2-1 if len(arr1) != len(arr2) else int(bool((sum(arr1)-sum(arr2))/abs(sum(arr1)-sum(arr2))+1))*2-1 if sum(arr1) != sum(arr2) else 0