def solution(num1, num2):
    return sum([num1 == num2]) * 2 - 1
    # return int(num1 == num2) * 2 - 1

print(f"값이 다를 경우: {solution(10, 20)}")
print(f"값이 같을 경우: {solution(10, 10)}")