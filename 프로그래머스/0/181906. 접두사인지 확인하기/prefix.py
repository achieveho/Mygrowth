def solution01(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))


def solution02(my_string, is_prefix):
    if my_string[:len(is_prefix)] == is_prefix:
        return 1
    return 0


def solution03(my_string, is_prefix):
    return 1 if my_string.find(is_prefix) == 0 else 0