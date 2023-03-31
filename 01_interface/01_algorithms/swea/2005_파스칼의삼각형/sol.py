# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P0-h6Ak4DFAUq

import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    matrix = [[0 for _ in range(N+2)] for _ in range(N+2)]
    matrix[2][1] = 1

    if N < 2:
        pass

    for row in range(1+2, N+2):
        for col in range(row):
            if col == 0 or col == row:
                matrix[row][col] = 0
            else:
                matrix[row][col] = matrix[row-1][col-1] + matrix[row-1][col]

    print(f'#{t}')
    for row in range(2, N+2):
        for col in range(1, row):
            if col == row-1 and col == 1:
                print(f'{matrix[row][col]}')
            elif col == row-1:
                print(f' {matrix[row][col]}')
            elif col == 1:
                print(f'{matrix[row][col]}', end = '')
            else:
                print(f' {matrix[row][col]}', end = '')
