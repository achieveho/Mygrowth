def solution01(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])

def solution02(my_string):
    return sorted(map(int, filter(lambda s: s.isdigit(), my_string)))

import re
def solution03(my_string):
    return sorted(map(int, (list(re.sub('[^0-9]', '', my_string)))))

def solution04(my_string):
    answer = []
    for i in my_string:
        if i.isdit():
            answer.append(int(i))
    answer.sort()
    
    return answer