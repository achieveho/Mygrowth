def solution(myString, pat):
    myString = myString.replace('A', 'a')
    myString = myString.replace('B', 'A')
    myString = myString.replace('a', 'B')
    print(myString)
    
    if pat in myString:
        return 1
    return 0