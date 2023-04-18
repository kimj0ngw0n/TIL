# https://www.acmicpc.net/problem/10811
N, M = map(int, input().split())

baskets = [_ for _ in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1

    tmp = baskets[i:j+1]
    x = 0
    for k in range(j, i-1, -1):
        baskets[k] = tmp[x]
        x += 1

print(baskets[0], end='')
for i in range(1, N):
    print(f' {baskets[i]}', end='')
