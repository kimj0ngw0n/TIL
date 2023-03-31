# https://school.programmers.co.kr/learn/courses/30/lessons/120812

def solution(array):
    mode = 0
    for i in array:
        if array.count(i) > array.count(mode):
            mode = i
    for i in array:
        if array.count(i) == array.count(mode):
            if i == mode:
                continue
            elif i != mode:
                return -1
    return mode


print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2, 3, 3]))
print(solution([2, 3, 1]))
