def solution01(my_string, num1, num2):
    [a, b] = sorted([num1, num2])
    return my_string[0:a] + my_string[b] + my_string[a + 1:b] + my_string[a] + my_string[b + 1:]