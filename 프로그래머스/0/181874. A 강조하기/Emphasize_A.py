def solution01(myString):
    return myString.lower().replace('a', 'A')


def solution02(myString):
    return ''.join([i.lower() if i != 'a' and i != 'A' else i.upper() for i in myString])


def solution03(myString):
    answer = []
    for i in myString:
        if i in ('a', 'A'):
            answer.append('A')
        else:
            answer.append(i.lower())
    
    return ''.join(answer)