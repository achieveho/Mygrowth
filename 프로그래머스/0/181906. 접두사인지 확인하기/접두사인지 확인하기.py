def solution(my_string, is_prefix):
    if (my_string[0] == is_prefix[0]) and (is_prefix[:] == my_string[:len(is_prefix)]):
        return 1
    return 0