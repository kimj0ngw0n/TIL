# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq

import sys
sys.stdin = open('input.txt')


def move_snail(pos, dir):
    return [pos[0]+dir[0], pos[1]+dir[1]]


def next_dir(prev_dir):
    prev_dir = tuple(prev_dir)
    # 우하좌상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    if prev_dir == (dr[0], dc[0]):
        return [dr[1], dc[1]]
    elif prev_dir == (dr[1], dc[1]):
        return [dr[2], dc[2]]
    elif prev_dir == (dr[2], dc[2]):
        return [dr[3], dc[3]]
    else:
        return [dr[0], dc[0]]


def can_move(matrix, pos, dir):
    nxt_pos = move_snail(pos, dir)
    # 벽에 막히거나 자기 몸통에 막히면 False
    if nxt_pos[0] == -1 or nxt_pos[1] == -1 or nxt_pos[0] == len(matrix) or nxt_pos[1] == len(matrix) or matrix[nxt_pos[0]][nxt_pos[1]]:
        return False
    else:
        return True


# main
T = int(input())

for t in range(1, T+1):
    N = int(input())
    now = [0, 0]
    dir = [0, 1]

    matrix = [[0 for _ in range(N)] for _ in range(N)]
    matrix[0][0] = 1

    for idx in range(2, N * N + 1):
        if can_move(matrix, now, dir):
            now = move_snail(now, dir)
            matrix[now[0]][now[1]] = idx
        else:
            dir = next_dir(dir)
            now = move_snail(now, dir)
            matrix[now[0]][now[1]] = idx

    print(f'#{t}')

    for row in range(N):
        for col in range(N):
            if not col:
                print(f'{matrix[row][col]}', end='')
            else:
                print(f' {matrix[row][col]}', end='')
        print('')
