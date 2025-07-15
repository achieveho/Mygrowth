def solution01(n_str):
    return str(int(n_str))


def solution02(n_str):
    for i in range(len(n_str)):
        if n_str[i] != "0":
            return n_str[i:]
        

def solution03():
    return lambda x: str(int(x))