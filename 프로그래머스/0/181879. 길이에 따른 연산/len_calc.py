from math import prod
from functools import reduce

def solution01(num_list):
    # prod 메서드는 주어진 iterable의 모든 원소를 곱한 결과를 반환.
    return sum(num_list) if len(num_list)>=11 else prod(num_list)


def solution02(num_list):
    # reduce 메서드는 iterable 객체의 모든 요소를 하나의 값으로 축약하는 고차 함수.
    # 첫 번째 인자: 인수를 받아 동작하는 함수.
    # 두 번째 인자: 처리할 iterable 객체
    # 세 번째 인자: 초기값 (선택 사항)
    return sum(num_list) if len(num_list)>=11 else reduce(lambda a, b: a * b, num_list)