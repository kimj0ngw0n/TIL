# https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):

    day = now= 0
    answer = []

    while now != len(progresses):
        day += 1
        cnt = 0
        for i in range(now, len(progresses)):
            pro = progresses[i] + speeds[i] * day
            if pro > 99:
                now += 1
                cnt += 1
            else:
                break
        if cnt:
            answer.append(cnt)

    return answer
