# https://school.programmers.co.kr/learn/courses/30/lessons/42747?language=python3

# 제한사항
# 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
# 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

# citations	        return
# [3, 0, 6, 1, 5]	3

def solution(citations):
    citations.sort(reverse=True)
    # print(citations)

    for i in range(len(citations)):
        print(i, citations[i])
        if i >= citations[i]:
            return i

    return len(citations)


citations1 = [3, 0, 6, 1, 5]
result = solution(citations1)
print(result)
