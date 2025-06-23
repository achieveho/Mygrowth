def solution(my_string):
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    result = []
    for i in range(len(my_string)):
        if my_string[i] in num:
            result.append(int(my_string[i]))
    result.sort()
    
    return result