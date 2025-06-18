def solution01(n, numlist):
    return list(filter(lambda v: v % n == 0, numlist))

def solution02(n, numlist):
    return [i for i in numlist if i % n == 0]
     
