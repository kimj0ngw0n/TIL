# https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    for idx, priority in enumerate(priorities):
        priorities[idx] = [priority, idx]

    answer = []
    while not answer or answer[-1] != location:
        maxpri = max(map((lambda x: x[0]), priorities))
        if priorities[0][0] == maxpri:
            answer.append(priorities[0][1])
            del priorities[0]
        else:
            maxidx = list(map((lambda x: x[0]), priorities)).index(maxpri)
            priorities = priorities[maxidx:] + priorities[:maxidx]


    return answer.index(location) + 1
