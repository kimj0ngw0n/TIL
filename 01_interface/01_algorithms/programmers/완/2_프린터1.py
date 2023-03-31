# https://school.programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):
    answer = 1

    while True:
        if location:
            select_prio = priorities.pop(0)
            if priorities and select_prio < max(priorities):
                priorities.append(select_prio)
            else:
                answer += 1
            location -= 1
        else:
            select_prio = priorities.pop(0)
            if priorities and select_prio < max(priorities):
                priorities.append(select_prio)
                location = len(priorities) - 1
            else:
                return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
print(solution([1], 0))
