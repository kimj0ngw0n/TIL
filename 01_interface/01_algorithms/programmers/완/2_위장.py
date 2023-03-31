# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    cloth_types = set(list(map(lambda x: x[1], clothes)))

    m = 1
    for cloth_type in cloth_types:
        cnt = list(map(lambda x: x[1], clothes)).count(cloth_type)
        m *= cnt + 1

    return m - 1
