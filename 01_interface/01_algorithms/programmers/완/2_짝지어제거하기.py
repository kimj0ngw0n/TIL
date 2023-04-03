# https://school.programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    s = list(s)
    box = []
    while s:
        l = s.pop()
        if box and box[-1] == l:
            del(box[-1])
        else:
            box.append(l)

    return int(not box)
