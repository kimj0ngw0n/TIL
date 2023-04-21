# https://www.acmicpc.net/problem/10798
L = []
for _ in range(5):
    L.append(input())

for j in range(15):
    for i in range(5):
        if len(L[i]) > j:
            print(L[i][j], end='')
