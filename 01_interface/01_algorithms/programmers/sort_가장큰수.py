# https://school.programmers.co.kr/learn/courses/30/lessons/42746?language=python3

# 제한 사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

# numbers	return
# [6, 10, 2]	"6210"
# [3, 30, 34, 5, 9]	"9534330"


def a_is_bigger_than_b(a, b):
    return True if int(str(a) + str(b)) - int(str(b) + str(a)) > 0 else False


def solution(numbers):
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if a_is_bigger_than_b(numbers[j], numbers[i]):
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp

    # print(numbers)
    str_numbers = []
    for number in numbers:
        str_numbers.append(str(number))

    answer = ''.join(str_numbers)

    return str(int(answer))


numbers1 = [6, 10, 2]
result = solution(numbers1)
print(result)
