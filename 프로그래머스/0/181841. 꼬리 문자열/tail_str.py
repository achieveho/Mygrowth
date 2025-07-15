def solution01(str_list, ex):
    return ''.join(filter(lambda x: ex not in x, str_list))


def solution02(str_list, ex):
    return ''.join([i for i in str_list if ex not in i])