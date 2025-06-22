def solution01(rsp):
    d = {'0': '5', '2': '0', '5': '2'}

    return ''.join(d[i] for i in rsp)

def solution02(rsp):
    rsp = rsp.replace('2', 's')
    rsp = rsp.replace('5', 'p')
    rsp = rsp.replace('0', 'r')
    rsp = rsp.replace('r', '5')
    rsp = rsp.replace('s', '0')
    rsp = rsp.replace('p', '2')

    return rsp

def solution03(rsp):
    return rsp.translate(str.maketrans('025', '502'))