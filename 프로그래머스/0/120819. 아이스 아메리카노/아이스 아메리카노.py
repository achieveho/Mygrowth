def solution(money):
    cafe = []
    cup, change = money // 5500, money % 5500
    cafe = cup, change
    
    return cafe