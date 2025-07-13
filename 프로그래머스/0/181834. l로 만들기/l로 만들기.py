def solution(myString):
    for i in myString:
        if ord(i) < ord('l'):
            myString = myString.replace(i, 'l')
        else:
            pass
        
    return myString