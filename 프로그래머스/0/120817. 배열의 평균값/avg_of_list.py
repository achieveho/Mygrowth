def solution(numbers):
    if not (1 <= len(numbers) <= 100):
        return None
    if not all(0 <= x <= 1000 for x in numbers):
        return None
    
    avg = sum(numbers) / len(numbers)
    rounded_avg = round(avg * 2) / 2
    return rounded_avg

print(solution([101, 103, 104]))

print(round(77.125 * 2 / 2))