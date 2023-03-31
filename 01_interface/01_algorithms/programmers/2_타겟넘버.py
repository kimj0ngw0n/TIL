# https://school.programmers.co.kr/learn/courses/30/lessons/43165

# pm : 더해야 하는지 빼야하는지
# total : index까지 계산 결과
# answer : target에 도달한 갯수

def cal(numbers, pm, total, target, answer):
    if not numbers:
        if total == target:
            answer += 1
            pm *= -1

    return numbers, pm, total, target, answer


def solution(numbers, target):
    answer = 0



    return answer