def solution01(array):
    return sorted(array)[len(array) // 2]       # 꼭 내림차순으로 하지 않아도 괜찮음.

def solution02(array):
    array.sort()
    return array[len(array) // 2]