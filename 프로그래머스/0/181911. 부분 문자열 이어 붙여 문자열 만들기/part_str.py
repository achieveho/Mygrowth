def solution01(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        s, e = parts[i]
        answer += my_strings[i][s:e + 1]

    return answer

def solution02(my_strings, parts):
    return ''.join([x[y[0]:y[1] + 1] for x, y in zip(my_strings, parts)])

def solution03(my_strings, parts):
    answer = ''
    for i in range(len(parts)):
        answer += (my_strings[i][parts[i][0]:parts[i][1] + 1])
    
    return answer

def solution04(my_strings, parts):
    return ''.join(my_strings[i][parts[i][0]:parts[i][1] + 1] for i in range(len(my_strings)))