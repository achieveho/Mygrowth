def solution01(my_string):
    return my_string.swapcase()

def solution02(my_string):
    answer = ''
    
    for i in my_string:
        if i.isupper():
            answer += i.lower()
        else:
            answer += i.upper()
    
    return answer

def solution03(my_string):
    return ''.join([x.lower() if x.isupper() else x.upper() for x in my_string])

def solution04(my_string):
    answer = ''

    for i in my_string:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            answer += chr(ord(i) - 32)
        elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
            answer += chr(ord(i) + 32)
        
    return answer