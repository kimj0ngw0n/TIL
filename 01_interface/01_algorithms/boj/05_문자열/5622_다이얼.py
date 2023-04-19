# https://www.acmicpc.net/problem/5622
A = input()
total = 0

for a in A:
    if a in 'S':
        total += 8
    elif a in 'TUV':
        total += 9
    elif a in 'WXYZ':
        total += 10
    else:
        b = (ord(a) - 65) // 3
        total += b + 3

print(total)
