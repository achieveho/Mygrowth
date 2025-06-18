def solution01(num_list):
    s = sum(num_list) ** 2
    m = eval('*'.join([str(n) for n in num_list]))

    return 1 if s > m else 0

def solution02(num_list):
    mul = 1
    for n in num_list:
        mul *= n
    
    return int(mul < sum(num_list) ** 2)