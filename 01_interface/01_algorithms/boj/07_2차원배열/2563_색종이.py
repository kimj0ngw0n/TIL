# https://www.acmicpc.net/problem/2563
blacks = set()
N = int(input())

for _ in range(N):
    x, y = map(int, input().split())

    for i in range(10):
        for j in range(10):
            blacks.add((x + i, y + j))

print(len(blacks))
