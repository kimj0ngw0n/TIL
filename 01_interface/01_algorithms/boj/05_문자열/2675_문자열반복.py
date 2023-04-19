# https://www.acmicpc.net/problem/2675
T = int(input())

R, S = input().split()
R = int(R)
for s in S:
    print(s * R, end='')

for _ in range(T-1):
    print('\n', end='')
    R, S = input().split()
    R = int(R)
    for s in S:
        print(s * R, end='')
