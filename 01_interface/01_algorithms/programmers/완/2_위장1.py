# https://school.programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    names = set()
    for cloth in clothes:
        names.add(cloth[1])

    num = dict()
    for cloth in clothes:
        name = cloth[1]
        if name in num.keys():
            num[name] += 1
        else:
            num[name] = 2

    answer = 1
    for key in num.keys():
        answer *= num[key]
    answer -= 1

    return answer
