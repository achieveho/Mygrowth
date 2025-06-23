def solution01(cipher, code):
    answer = cipher[code-1::code]
    
    return answer