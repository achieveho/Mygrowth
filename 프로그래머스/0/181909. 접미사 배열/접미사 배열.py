from typing import List

def solution(my_string: str) -> List[str]:
    n = len(my_string)
    suffixes: List[str] = [my_string[i:] for i in range(n)]
    suffixes.sort()
    
    return suffixes