def solution(myString, pat):
    my_string, pat = myString.lower(), pat.lower()
    if pat in my_string:
        return 1
    return 0