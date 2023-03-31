# https://school.programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):
    answer = 0

    while True:
        select_prio = priorities.pop(0)
        if priorities and select_prio < max(priorities):
            priorities.append(select_prio)
        else:
            answer += 1
            if not location:
                return answer

        if location:
            location -= 1
        else:
            location = len(priorities) - 1


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
print(solution([1], 0))
