def solution(my_string, alp):
    if alp in my_string:
        my_string = my_string.replace(alp, alp.upper())
    else:
        None
    return my_string