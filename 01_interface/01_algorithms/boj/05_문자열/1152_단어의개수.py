# https://www.acmicpc.net/problem/1152
S = input().strip()
if S == ' ':
    print(0)
else:
    print(S.count(' ') + 1)

# print(len(input().split()))
