# https://school.programmers.co.kr/learn/courses/30/lessons/120817
def solution(numbers):
    answer = 0

    for num in numbers:
        answer += num

    return answer / (len(numbers))
