# https://www.acmicpc.net/problem/25304
X = int(input())

N = int(input())

val = 0
for _ in range(N):
    a, b = list(map(int, input().split()))
    val += a * b

print('Yes') if val == X else print('No')
