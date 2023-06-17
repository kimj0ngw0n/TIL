# https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3

def solution(nums):
    ponkets_set = set(nums)
    ponkets_set_len = len(ponkets_set)
    get_ponkets_len = len(nums) // 2

    answer = min(ponkets_set_len, get_ponkets_len)

    return answer
