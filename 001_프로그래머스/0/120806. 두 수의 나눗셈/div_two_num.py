# lambda 사용하기.
def solution(num1, num2):
    if (0 < num1 <= 100) and (0 < num2 <= 100):
        return lambda num1, num2: 1000 * num1 // num2