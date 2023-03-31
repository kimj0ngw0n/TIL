# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):

    for h in range(len(citations), 0, -1):
        total = sum([1 if x >= h else 0 for x in citations])
        if total >= h:
            break

    return min(h, total)
