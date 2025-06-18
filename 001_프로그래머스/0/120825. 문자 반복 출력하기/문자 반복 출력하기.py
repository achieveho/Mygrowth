def solution(my_string, n):
    mul = ""
    for i in range(len(my_string)):
        mul += my_string[i] * n
    
    return mul