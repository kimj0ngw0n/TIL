# https://school.programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    day = idx = 0
    answer = []

    while idx == len(progresses):
        day += 1
        cnt = 0
        for i in range(idx, len(progresses)):
            if progresses[i] + day * speeds[i] >= 100:
                idx += 1
                cnt += 1
            else:
                break
        if cnt:
            answer.append(cnt)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
