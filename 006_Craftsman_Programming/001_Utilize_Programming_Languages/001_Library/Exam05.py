# 문제 05.
# 다음은 dictionary 변수에 어떤 값이 value로 포함되어 있다면, 해당 value의 key 값을 모두 찾아 반환하는 Python 프로그램이다.
# 괄호 안에 들어갈 알맞은 method를 작성하시오.
def test(dict, x):
    return [k for k, v in dict.keys() if v == x]