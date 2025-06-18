def solution(my_string):
    ch = ['a', 'e', 'i', 'o', 'u']
    new_string = my_string
    for i in range(len(my_string)):
        if my_string[i] in ch:
            new_string = new_string.replace(my_string[i], "")
        else:
            continue
    return new_string