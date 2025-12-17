# 006 파일에서 쓸 모듈 생성을 위한 'diet.py'
menu = {"고구마": 200, "떡볶이": 600, "라면": 800}

def get_recommend_weight(height, man = True):
    weight = 0
    if man:
        weight = (height - 100) * 0.9
    else:
        weight = height - 100
    print(f"권장 체중은 {weight}kg 입니다.")

    return weight

def print_valid_menu():
    for key, value in menu.items():
        if value > 500:
            print(f"{key}: X")
        else:
            print(f"{key}: O")