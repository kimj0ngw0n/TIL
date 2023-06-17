# https://school.programmers.co.kr/learn/courses/30/lessons/42587?language=python3

# 규칙
# 1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
# 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
# 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
#   3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.

# 제한사항
# priorities의 길이는 1 이상 100 이하입니다.
# priorities의 원소는 1 이상 9 이하의 정수입니다.
# priorities의 원소는 우선순위를 나타내며 숫자가 클 수록 우선순위가 높습니다.
# location은 0 이상 (대기 큐에 있는 프로세스 수 - 1) 이하의 값을 가집니다.
# priorities의 가장 앞에 있으면 0, 두 번째에 있으면 1 … 과 같이 표현합니다.

# 입출력 예
# priorities	location	return
# [2, 1, 3, 2]	2	1
# [1, 1, 9, 1, 1, 1]	0	5

def solution(priorities, location):
    count = 0

    while True:
        if len(priorities) == 0:
            break

        max_process = max(priorities)  # 전체 프로세스 중 최댓값
        now_process = priorities.pop(0)  # 현재 프로세스
        location -= 1

        if now_process < max_process:
            priorities.append(now_process)
            if location < 0:
                location = len(priorities)-1
        else:
            count += 1
            if location < 0:
                return count

        # print(priorities, location)


priorities1 = [2, 1, 3, 2]
location1 = 2
print(solution(priorities1, location1))
