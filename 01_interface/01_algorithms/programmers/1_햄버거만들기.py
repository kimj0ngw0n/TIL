# https://school.programmers.co.kr/learn/courses/30/lessons/133502

# def solution(ingredient):

#     answer = 0
#     hamset = [1, 2, 3, 1]
#     list_sangsu = []

#     for food in ingredient:
#         list_sangsu.append(food)
#         if len(list_sangsu) >= 4:
#             if list_sangsu[-4:] == hamset:
#                 answer += 1
#                 list_sangsu = list_sangsu[:-3]

#     return answer


def solution(ingredient):
    answer = 0
    hamset = [1, 2, 3, 1]
    list_sangsu = []

    for food in ingredient:
        list_sangsu.append(food)
        if len(list_sangsu) >= 4:
            if list_sangsu[-4:] == hamset:
                answer += 1
                for _ in range(4):
                    list_sangsu.pop()

    return answer


# 2
print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))

# 0
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))
