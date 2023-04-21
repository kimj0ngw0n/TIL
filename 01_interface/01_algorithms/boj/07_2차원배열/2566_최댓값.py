# https://www.acmicpc.net/problem/2566
L = []
v = 0
r = c = 1

for i in range(9):
    L = list(map(int, input().split()))
    for j in range(9):
        if L[j] > v:
            v = L[j]
            r = i+1
            c = j+1

print(v)
print(f'{r} {c}')
