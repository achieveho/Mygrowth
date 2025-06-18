def solution(sides):
    sides.sort(reverse = True)
    while sides:
        if sides[0] < sum(sides[1:]):
            return 1
        return 2