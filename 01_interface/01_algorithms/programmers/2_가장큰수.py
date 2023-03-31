# https://school.programmers.co.kr/learn/courses/30/lessons/42746
def solution(numbers):

    new_numbers = []
    # 모든 숫자를 네 자리로 만들기
    for i, number in enumerate(numbers):
        while number < 1000:
            number *= 10
        new_numbers.append([numbers[i], number])

    # 네 자리 숫자를 기준으로 정렬
    new_numbers.sort(key=lambda x: x[1])

    answer = ''
    number_add = []
    while new_numbers:
        number_add.append(new_numbers.pop())
        while new_numbers and number_add:
            if number_add[0][1] == new_numbers[-1][1]:
                number_add.append(new_numbers.pop())
                number_add.sort(key=lambda x: x[0])
            else:
                break
        for i in range(len(number_add)):
            answer += str(number_add[i][0])
        number_add = []

    return answer


print(solution([3, 30, 34, 5, 9]))
