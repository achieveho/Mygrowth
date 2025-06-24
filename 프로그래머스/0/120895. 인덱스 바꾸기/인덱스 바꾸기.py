def solution(my_string, num1, num2):
    calc = list(my_string)
    calc[num1], calc[num2] = calc[num2], calc[num1]
    
    return ''.join(calc)