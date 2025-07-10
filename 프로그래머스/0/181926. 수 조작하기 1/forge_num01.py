def solution01(n, control):
    key = dict(zip(['w', 's', 'd', 'a'], [1, -1, 10, -10]))

    return n + sum([key[c] for c in control])


def solution02(n, control):
    c = {'w':1, 's':-1, 'd':10, 'a':-10}
    for i in control:
        n += c[i]
    
    return n


def solution03(n, control):
    return n + 10 * (control.count('d') - control.count('a')) + (control.count('w') - control.count('s'))
