# https://www.acmicpc.net/problem/8393
n = int(input())

k = n // 2

if n % 2:
    print((n + 1) * k + k + 1)
else:
    print((n + 1) * k)
