def solution01(my_string, index_list):
    return ''.join([my_string[idx] for idx in index_list])


def solution02(my_string, index_list):
    answer = ''
    for i in index_list:
        answer += my_string[i]
    
    return answer