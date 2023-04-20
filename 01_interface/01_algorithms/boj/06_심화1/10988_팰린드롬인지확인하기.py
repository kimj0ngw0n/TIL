# https://www.acmicpc.net/problem/10988
S = input()

flag = True
for i in range(len(S) // 2):
    if S[i] != S[-(i+1)]:
        print(0)
        flag = False
        break

if flag:
    print(1)
