# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc

import sys
sys.stdin = open('input.txt')

T = int(input())

for count in range(T):

    N = int(input())
    future = list(map(int, input().split()))
    now = []
    total = maximum = 0

    while future:
        maximum = max(future)
        max_idx = future.index(maximum)
        now = future[0:max_idx]
        future = future[max_idx+1:]

        total += maximum * len(now) - sum(now)

    print(f'#{count+1} {total}')
