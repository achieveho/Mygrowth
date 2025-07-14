def solution01(arr, delete_list):
    return [i for i in arr if i not in delete_list]


def solution02(arr, delete_list):
    return list(filter(lambda x: x not in delete_list, arr))