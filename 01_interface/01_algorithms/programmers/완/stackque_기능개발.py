# https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=python3

# 제한 사항
# 작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
# 작업 진도는 100 미만의 자연수입니다.
# 작업 속도는 100 이하의 자연수입니다.
# 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

# 입출력 예
# progresses	speeds	return
# [93, 30, 55]	[1, 30, 5]	[2, 1]
# [95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]


def solution(progresses, speeds):
    answer = []
    end_index = 0  # 배포가 끝난 index

    while end_index < len(progresses):
        count = 0

        # 실제 진척도를 더해주는 반복문
        for i in range(end_index, len(progresses)):
            progresses[i] += speeds[i]
        # print(progresses, answer)

        # 완료 여부를 체크하는 반복문
        for i in range(end_index, len(progresses)):
            if progresses[i] >= 100:
                count += 1
                end_index += 1
            else:
                break

        if count:
            answer.append(count)

    return answer


progresses1 = [95, 90, 99, 99, 80, 99]
speeds1 = [1, 1, 1, 1, 1, 1]
result = solution(progresses1, speeds1)
print(result)
