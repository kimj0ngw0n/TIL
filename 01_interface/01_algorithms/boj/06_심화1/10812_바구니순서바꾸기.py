# https://www.acmicpc.net/problem/10812
N, M = map(int, input().split())

baskets = [_ for _ in range(1, N+1)]

for _ in range(M):
    i, j, k = map(int, input().split())
    tmp1 = baskets[i-1:k-1]
    tmp2 = baskets[k-1:j]
    baskets[i-1:j] = tmp2 + tmp1

print(baskets[0], end='')
for i in range(1, N):
    print(f' {baskets[i]}', end='')
