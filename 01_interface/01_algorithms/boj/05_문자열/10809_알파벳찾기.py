# https://www.acmicpc.net/problem/10809
S = input()
result = [-1 for _ in range(26)]
for i, s in enumerate(S):
    if result[ord(s)-97] == -1:
        result[ord(s)-97] = i

print(result[0], end='')
for i in range(1, 26):
    print(f' {result[i]}', end='')
