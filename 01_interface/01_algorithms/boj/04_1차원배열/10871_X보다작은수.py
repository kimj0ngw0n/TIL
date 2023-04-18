# https://www.acmicpc.net/problem/10871
N, X = map(int, input().split())

A = list(map(int, input().split()))

result = []
for a in A:
    if a < X:
        result.append(a)

print(result[0], end='')
for i in range(len(result)):
    if i:
        print(f' {result[i]}', end='')
