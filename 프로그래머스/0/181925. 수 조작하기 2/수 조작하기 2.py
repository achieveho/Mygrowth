def solution(numLog):
    s = ""
    current = numLog[0]
    for i in numLog[1:]:
        if i == current + 1:
            s += "w"
        elif i == current - 1:
            s += "s"
        elif i == current + 10:
            s += "d"
        else:
            s += "a"
        current = i
    return s