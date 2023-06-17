# https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=python3

# 제한사항
# 배열 arr의 크기 : 1,000,000 이하의 자연수
# 배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수

# 입출력 예
# arr	            answer
# [1,1,3,3,0,1,1]	[1,3,0,1]
# [4,4,4,3,3]	    [4,3]

def solution(arr):
    answer = [arr[0]]

    for number in arr[1:]:
        if (len(answer) != 0) & (answer[-1] != number):
            answer.append(number)

    return answer


print(solution([1,1,3,3,0,1,1]))
