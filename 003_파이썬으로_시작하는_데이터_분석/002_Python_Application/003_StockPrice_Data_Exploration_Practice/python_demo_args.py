"""
실행 방법:
- (권장) 터미널: python demo_args.py
- 또는 주피터 셀에 그대로 붙여넣고 실행

이 스크립트는 "정상 결과"와 "TypeError"를 의도적으로 섞어서
positional / keyword / keyword-only / positional-only / *args / **kwargs / unpacking을 한 방에 체감하게 합니다.
"""

from __future__ import annotations


def run_case(title, fn):
    print(f"\n=== {title} ===")
    try:
        result = fn()
        print("RESULT:", result)
    except Exception as e:
        print(f"EXCEPTION: {type(e).__name__}: {e}")


# 1) 기본: 위치 or 키워드 둘 다 가능 (/, * 없을 때)
def basic(a, b, c=0):
    return {"a": a, "b": b, "c": c}


# 2) 키워드 전용: * 뒤에 오는 인자는 반드시 이름=값 으로만 전달 가능
def kw_only(*, dropna=True, q=0.9):
    return {"dropna": dropna, "q": q}


# 3) 위치 전용: / 앞에 오는 인자는 반드시 위치로만 전달 가능 (키워드로 못 줌)
def pos_only(a, b, /, c):
    return {"a": a, "b": b, "c": c}


# 4) 혼합: 위치 전용 / 위치-or-키워드 / 키워드 전용
def mixed(p1, p2, /, p3, *, k1, k2="K2"):
    return {"p1": p1, "p2": p2, "p3": p3, "k1": k1, "k2": k2}


# 5) *args, **kwargs: 남는 인자를 수집 (그리고 *args 뒤 파라미터는 keyword-only가 될 수 있음)
def varargs(a, *args, sep=",", **kwargs):
    """
    a: 첫 번째는 필수
    *args: 남는 위치 인자들을 튜플로 수집
    sep: *args 뒤에 있으므로 keyword-only로 쓰는 게 안전/명확
    **kwargs: 남는 키워드 인자들을 dict로 수집
    """
    return {
        "a": a,
        "args": args,
        "sep": sep,
        "kwargs": kwargs,
    }


# 6) 타입 어노테이션(return annotation)은 "강제"가 아니라 "메타데이터" 성격임을 보여주는 예시
def annotated_return(x: int) -> tuple[float, int]:
    # 일부러 규약과 다르게 반환해도(예: str) 런타임에서 강제되지 않음을 체감하려면 아래를 바꿔보세요.
    return (float(x) / 2, x)


# -------------------------
# 케이스 실행 (정상/오류 섞기)
# -------------------------
if __name__ == "__main__":

    # [A] basic: 위치/키워드
    run_case("1) basic: 전부 위치 인자", lambda: basic(1, 2, 3))
    run_case("2) basic: 일부 키워드 인자", lambda: basic(1, b=2, c=3))
    run_case("3) basic: 키워드 순서 바꿔도 OK", lambda: basic(c=30, b=20, a=10))

    # 오류: 인자 중복 전달(같은 파라미터에 positional + keyword)
    run_case("4) basic: 중복 전달(에러)", lambda: basic(1, 2, b=99))

    # 오류: 존재하지 않는 키워드 인자
    run_case("5) basic: 알 수 없는 키워드(에러)", lambda: basic(1, 2, d=4))

    # [B] 키워드 전용: kw_only
    run_case("6) kw_only: 키워드로만 정상", lambda: kw_only(dropna=False, q=0.95))
    run_case("7) kw_only: 위치로 넣으면 에러", lambda: kw_only(False, 0.95))

    # [C] 위치 전용: pos_only
    run_case("8) pos_only: 정상(앞 2개 위치)", lambda: pos_only(1, 2, 3))
    run_case("9) pos_only: a를 키워드로 주면 에러", lambda: pos_only(a=1, b=2, c=3))

    # [D] 혼합: mixed
    run_case("10) mixed: 정상 호출(앞 2개 위치, k1은 키워드)", lambda: mixed(1, 2, 3, k1="K1"))
    run_case("11) mixed: k1을 위치로 주면 에러", lambda: mixed(1, 2, 3, "K1"))

    # [E] *args / **kwargs 수집
    run_case(
        "12) varargs: *args(남는 위치) + **kwargs(남는 키워드) 수집",
        lambda: varargs("A", 10, 20, 30, sep="|", foo=1, bar=2),
    )

    # [F] 언패킹: 호출에서 * / ** 사용
    pos_list = [10, 20, 30]
    kw_dict = {"sep": "::", "foo": "X"}

    run_case("13) varargs: *리스트로 위치 언패킹", lambda: varargs("A", *pos_list))
    run_case("14) varargs: **딕셔너리로 키워드 언패킹", lambda: varargs("A", **kw_dict))
    run_case("15) varargs: * + ** 같이 쓰기", lambda: varargs("A", *pos_list, **kw_dict))

    # 오류: **에 없는 키워드가 함수에 전달되면(또는 중복 키워드) TypeError
    dup_kw = {"sep": "!!", "foo": 1}
    run_case("16) varargs: sep 중복 전달(에러)", lambda: varargs("A", sep="|", **dup_kw))

    # [G] 어노테이션은 강제 규칙이 아니라 메타데이터(도구가 활용)
    run_case("17) annotated_return 정상 실행", lambda: annotated_return(10))
    run_case("18) __annotations__ 확인", lambda: annotated_return.__annotations__)