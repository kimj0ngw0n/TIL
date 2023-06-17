# https://school.programmers.co.kr/learn/courses/30/lessons/42746?language=python3

# 제한 사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

# numbers	return
# [6, 10, 2]	"6210"
# [3, 30, 34, 5, 9]	"9534330"

from functools import cmp_to_key
# cmp_to_key : 커스텀 정렬할 수 있도록 도와주는 헬퍼 함수
# cmp_to_key 의 return : 음수(-1)=뒤가 크다, 0=같다, 양수(1)=앞이 크다
# cmp_to_key lambda의 x, y는 비교할 값이 들어간다.

def solution(numbers):
    numbers.sort(key=cmp_to_key(lambda x, y: int(str(y) + str(x)) - int(str(x) + str(y))))
    # print(numbers)

    str_numbers = []
    for number in numbers:
        str_numbers.append(str(number))

    answer = ''.join(str_numbers)

    return str(int(answer))


# numbers = [6, 10, 2]
numbers = [0, 0, 0]
result = solution(numbers)
print(result)
