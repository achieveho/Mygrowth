def solution01(my_string):
    return ''.join(sorted(my_string.lower()))

def solution02(my_string):
    answer = []
    for i in my_string:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            answer.append(chr(ord(i) + 32))
        else:
            answer.append(i)
    
    return ''.join(sorted(answer))