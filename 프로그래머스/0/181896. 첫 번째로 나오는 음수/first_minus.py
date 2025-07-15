def solution01(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    return -1


def solution02(num_list):
    return ([i for i in range(len(num_list)) if num_list[i] < 0] or [-1])[0]