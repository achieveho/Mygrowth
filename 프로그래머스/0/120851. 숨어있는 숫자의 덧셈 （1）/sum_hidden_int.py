def solution01(my_string):
    answer = 0
    for i in my_string:
        try:
            answer += int(i)
        except:
            pass
    
    return answer

import re

def solution02(my_string):
    return sum(int(n) for n in re.sub('[^1-9]', '', my_string))

def solution03(my_string):
    answer = 0
    for i in my_string:
        if i.isnumeric():
            answer += int(i)
    
    return answer

def solution04(my_string):
    answer = 0
    for i in my_string:
        if not i.isalpha():
            answer += int(i)
    
    return answer