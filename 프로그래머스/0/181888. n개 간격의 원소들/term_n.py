def solution01(num_list, n):
    return num_list[::n]

from itertools import compress
def solution02(num_list, n):
    return [num_list[i] for i in range(0, len(num_list), n)]