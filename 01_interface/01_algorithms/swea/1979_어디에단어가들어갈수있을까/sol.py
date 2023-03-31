# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq

import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())

    matrix = []

    for idx in range(N):
        matrix.append(list(map(int, input().split())))

    total = 0

    # row에 대해서 확인
    for row in range(N):
        tcount = [0]
        for col in range(N):
            if matrix[row][col]:
                tcount[-1] = tcount[-1] + 1
            else:
                tcount.append(0)
        total += tcount.count(K)

    # col에 대해서 확인
    for col in range(N):
        tcount = [0]
        for row in range(N):
            if matrix[row][col]:
                tcount[-1] = tcount[-1] + 1
            else:
                tcount.append(0)
        total += tcount.count(K)

    print(f'#{t} {total}')
