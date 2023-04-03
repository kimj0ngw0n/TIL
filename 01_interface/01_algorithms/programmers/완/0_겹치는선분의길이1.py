# https://school.programmers.co.kr/learn/courses/30/lessons/120876
def solution(lines):
    answer = 0
    dots = []

    for i, line in enumerate(lines):
        for dot in range(line[0], line[1]):
            dots.append(dot)

    for i in range(-100, 101):
        if dots.count(i) > 1:
            answer += 1

    return answer
