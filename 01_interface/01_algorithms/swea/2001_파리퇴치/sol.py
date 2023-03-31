import sys
sys.stdin = open('input.txt')


def kill_bug(matrix, M, start):
    total = 0
    for row in range(start[0], start[0]+M):
        for col in range(start[1], start[1]+M):
            total += matrix[row][col]
    return total


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    matrix = [[0 for _ in range(N)] for _ in range(N)]
    for row in range(N):
        matrix[row] = list(map(int, input().split()))
    #matrix = [list(map(int, input().split())) for _ in range(N)]

    maximum = 0
    for row in range(N-M+1):
        for col in range(N-M+1):
            num_kill = kill_bug(matrix, M, [row, col])
            if num_kill > maximum:
                maximum = num_kill

    print(f'#{t} {maximum}')
