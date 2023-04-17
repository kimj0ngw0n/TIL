# https://www.acmicpc.net/problem/10952
while True:
    A, B = list(map(int, input().split()))
    if not A and not B:
        break
    print(A + B)
