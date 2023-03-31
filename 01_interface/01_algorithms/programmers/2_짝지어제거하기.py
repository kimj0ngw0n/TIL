# https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    s = list(s)
    dels = []

    while s:
        dels.append(s.pop())
        if len(dels) > 1 and dels[-1] == dels[-2]:
            del(dels[-1])
            del(dels[-1])

    return int(not dels)


# 2차
# # https://school.programmers.co.kr/learn/courses/30/lessons/12973
#
# def solution(s):
#     s = list(s)
#     box = []
#     while s:
#         l = s.pop()
#         if box and box[-1] == l:
#             del(box[-1])
#         else:
#             box.append(l)
#
#     return int(not box)
