def solution(box, n):
    wid = box[0] // n
    ver = box[1] // n
    hei = box[2] // n
    
    return wid * ver * hei