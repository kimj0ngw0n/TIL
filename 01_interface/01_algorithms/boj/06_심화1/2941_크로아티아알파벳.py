# https://www.acmicpc.net/problem/2941
cro2 = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
cro3 = 'dz='
S = input()
i = result = 0

while i < len(S):
    if len(S) - i > 2:
        if S[i:i+3] == cro3:
            i += 3
            result += 1
            continue
    if len(S) - i > 1:
        if S[i:i+2] in cro2:
            i += 2
            result += 1
            continue
    i += 1
    result += 1

print(result)
