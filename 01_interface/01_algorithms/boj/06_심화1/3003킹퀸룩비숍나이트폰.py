# https://www.acmicpc.net/problem/3003
PIECES = [1, 1, 2, 2, 2, 8]

pieces = list(map(int, input().split()))

print(PIECES[0]-pieces[0], end='')
for i in range(1, len(PIECES)):
    print(f' {PIECES[i]-pieces[i]}', end='')
