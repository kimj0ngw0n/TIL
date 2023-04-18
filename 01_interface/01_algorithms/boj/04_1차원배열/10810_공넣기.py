# https://www.acmicpc.net/problem/10810
N, M = map(int, input().split())

result = [0 for _ in range(N)]
for _ in range(M):
    i, j, k = map(int, input().split())
    for idx in range(i-1, j):
        result[idx] = k

print(result[0], end='')
for i in range(1, N):
    print(f' {result[i]}', end='')
