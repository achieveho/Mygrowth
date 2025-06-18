def solution(num1, num2):
    def validate_input(x, lower, upper):
        if x >= lower and x <= upper:
            return True
        return False
    num_list = [num1, num2]
    assert all([validate_input(x, -50000, 50000) for x in num_list])
    answer = num1 - num2
    return answer