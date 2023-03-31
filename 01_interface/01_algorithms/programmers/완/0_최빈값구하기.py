# https://school.programmers.co.kr/learn/courses/30/lessons/120812

def solution(array):

    list_array = list(set(array))
    array_count = []

    for a in list_array:
        array_count.append(array.count(a))

    max_count = max(array_count)

    if array_count.count(max_count) > 1:
        return -1
    else:
        return list_array[array_count.index(max_count)]


print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2, 3, 3]))
print(solution([2, 3, 1]))
