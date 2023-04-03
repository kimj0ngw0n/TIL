# https://school.programmers.co.kr/learn/courses/30/lessons/120818
import math

def solution(price):
    if price < 100000:
        return price
    elif price < 300000:
        return math.trunc(price * 0.95)
    elif price < 500000:
        return math.trunc(price * 0.9)
    else:
        return math.trunc(price * 0.8)
