def solution01(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))


def solution02(num_list):
    odd, even = 0, 0

    for i, n in enumerate(num_list):
        if i % 2:
            even += n
        else:
            odd += n
    
    return max(even, odd)