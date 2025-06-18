def solution(my_string):
    if (1 <= len(my_string) <= 1000):
        # my_string = my_string[::-1]
        return my_string[::-1]

print(solution("jaron"))

def solution2(my_string):
    return ''.join(reversed(my_string))

print(solution2("Hello, World!!"))