"""
이 스크립트는 '정상 결과'와 'TypeError'를 의도적으로 섞어서
positional / keyword / keyword-only / positional-only / *args / **kwargs / unpacking을 한 번에 체감하게 해주는 코드.
"""

from __future__ import annotations

def run_case(title, fn):
    print(f"\n=== {title} ===")
    try:
        result = fn()
        print("RESULT:", result)
    except Exception as e:
        print(f"EXCEPTION: {type(e).__name__}: {e}")

# 01. 기본: 위치 인자와 키워드 인자 둘 다 사용 가능.
# '/'와 '*'가 없을 때 해당.
def basic(a, b, c=0):
    return {"a": a, "b": b, "c": c}

# 02. 키워드 인자 전용: '*' 뒤에 오는 인자는 반드시 '이름=값' 형태로만 전달 가능.
def kw_only(*, dropna=True, q=0.9):
    return {"dropna": dropna, "q": q}

# 03. 위치 인자 전용: '/' 앞에 오는 인자는 반드시 위치 인자로만 전달 가능. (키워드 인자는 사용 불가)
def pos_only(a, b, /, c):
    return {"a": a, "b": b, "c": c}

# 04. 혼합: 위치 인자, 위치 인자 전용, 키워드 인자, 키워드 인자 전용 혼합 사용
def mixed(p1, p2, /, p3, *, k1, k2="k2"):
    return {"p1": p1, "p2": p2, "p3": p3, "k1": k1, "k2": k2}

# 05. *args, **kwargs: 남는 인자들을 수집함. (*args 뒤의 파라미터는 키워드 인자 전용이 될 수 있음.)
def varargs(a, *args, sep=",", **kwargs):
    """
    a: 첫 번째 인자는 필수로 존재해야 함.
    *args: 남는 위치 인자들을 튜플로 수집함.
    sep: *args 뒤에 있기 때문에 키워드 인자 전용으로 사용하는 것이 안전하고 명확함.
    **kwargs: 남는 키워드 인자들을 dict 형태로 수집.
    """
    return {
        "a": a,
        "args": args,
        "sep": sep,
        "kwargs": kwargs,
    }

# 06. 타입 어노테이션(return annotation): 강제가 아닌 메타데이터 성격을 지님.
def annotated_return(x: int) -> tuple[float, int]:
    # 꼭 return이 float가 아니어도 runtime에서 강제되지 않음. (직접 타입 바꿔서 실행해보면 됨.)
    return (float(x) / 2, x)

if __name__ == "__main__":
    # 01. 기본 형태 사용 (위치 인자와 키워드 인자)
    run_case("1) basic: 전부 위치 인자", lambda: basic(1, 2, 3))
    run_case("2) basic: 일부는 키워드 인자", lambda: basic(1, b=2, c=3))
    run_case("3) basic: 키워드 인자의 순서를 바꾸는 것도 가능", lambda: basic(c=30, b=20, a=10))

    # 오류 01. 인자를 중복해서 전달. (같은 파라미터에 위치 인자와 키워드 인자를 사용.)
    run_case("4) basic: 중복 전달(에러)", lambda: basic(1, 2, b=99))

    # 오류 02. 존재하지 않는 키워드 인자 사용
    run_case("5) basic: 알 수 없는 키워드 인자 사용(에러)", lambda: basic(1, 2, d=4))

    # 02. 키워드 인자 전용.
    run_case("6) kw_only: 키워드 인자만 사용해야 함.", lambda: kw_only(dropna=False, q=0.95))
    run_case("7) kw_only: 위치 인자를 사용하면 에러 발생", lambda: kw_only(False, 0.95))

    # 03. 위치 인자 전용.
    run_case("8) pos_only: 위치 인자만을 사용해야 함.", lambda: pos_only(1, 2, 3))
    run_case("9) pos_only: '/' 앞의 인자를 키워드 인자로 전달하면 에러 발생", lambda: pos_only(a=1, b=2, c=3))

    # 04. 위치 인자 & 키워드 인자 혼합 사용
    run_case("10) mixed: 정상적인 혼합 사용", lambda: mixed(1, 2, 3, k1="k1"))
    run_case("11) mixed: k1에 위치 인자를 사용하면 에러 발생.", lambda: mixed(1, 2, 3, "k1"))

    # 05. *args와 **kwargs
    run_case("12) varargs: *args(남는 위치 인자) + **kwargs(남는 키워드 인자)를 수집.",
             lambda: varargs("a", 10, 20, 30, sep="|", foo=1, bar=2))
    
    # 06. Unpacking: 호출에서 '*' 또는 '**'를 사용하기.
    pos_list = [10, 20, 30]
    kw_dict = {"sep": "::", "foo": "X"}
    
    run_case("13) varargs: '*리스트'로 위치 인자를 unpacking", lambda: varargs("A", *pos_list))
    run_case("14) varargs: '**딕셔너리'로 키워드 인자를 unpacking", lambda: varargs("A", **kw_dict))
    run_case("15) varargs: '*'과 '**'를 같이 사용하기", lambda: varargs("A", *pos_list, **kw_dict))

    # 오류 03. '**'에 존재하지 않는 키워드 인자가 함수에 전달되거나 중복으로 키워드 인자가 전달될 경우 TypeError 발생.
    dup_kw = {"sep": "!!", "foo": 1}
    run_case("16) varargs: sep이 중복 전달되어 에러 발생", lambda: varargs("A", sep="|", **dup_kw))

    # 오류 04. annotation은 강제 규칙이 아닌 메타데이터.
    run_case("17) annotated_return이 정상 실행되는 경우", lambda: annotated_return(10))
    run_case("18) __annotations__ 확인", lambda: annotated_return.__annotations__)