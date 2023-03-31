# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):

    brown = int(brown / 2) - 2
    row = (brown + (brown ** 2 - 4 * yellow) ** (1/2)) / 2 + 2
    col = (brown - (brown ** 2 - 4 * yellow) ** (1 / 2)) / 2 + 2

    return [row, col]
