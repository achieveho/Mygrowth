def solution(arr, k):
    result = []
    for i in arr:
        if k % 2 == 1:
            result.append(i * k)
        else:
            result.append(i + k)
    
    return result
    