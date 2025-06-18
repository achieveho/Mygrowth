def solution01(number, n, m):
    return int(number % n == 0) & (number % m == 0)

print(solution01(10, 2, 5))