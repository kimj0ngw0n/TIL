# https://school.programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations):
    for h in range(max(citations), 0, -1):
        if len(list(filter(lambda x: x >= h, citations))) >= h:
            return h
    return 0




print(solution([3, 0, 6, 1, 5]))
print(solution([6, 6, 6]))
