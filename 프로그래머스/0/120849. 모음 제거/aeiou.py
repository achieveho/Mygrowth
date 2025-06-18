import re

def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])

def solution01(my_string):
    return re.sub('[aeiou]', "", my_string)

def solution02(my_string):
    return re.sub(r"a|e|i|o|u", "", my_string)

def solution03(my_string):
    answer = ""
    for i in my_string:
        if i not in ['a', 'e', 'i', 'o', 'u']:
            answer += i
    return answer