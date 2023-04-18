# https://www.acmicpc.net/problem/10813
N, M = map(int, input().split())

basket = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    tmp = basket[i]
    basket[i] = basket[j]
    basket[j] = tmp

print(basket[0], end='')
for i in range(1, N):
    print(f' {basket[i]}', end='')
