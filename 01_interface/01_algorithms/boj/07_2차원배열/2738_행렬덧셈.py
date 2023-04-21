# https://www.acmicpc.net/problem/2738
N, M = map(int, input().split())

A = []
B = []

for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(N):
    B.append(list(map(int, input().split())))

R = []
for i in range(N):
    r = []
    for j in range(M):
        r.append(A[i][j] + B[i][j])
    R.append(r)

print(R[0][0], end='')

for j in range(1, M):
    print(f' {R[0][j]}', end='')

for i in range(1, N):
    print('\n', end='')
    print(f'{R[i][0]}', end='')
    for j in range(1, M):
        print(f' {R[i][j]}', end='')
