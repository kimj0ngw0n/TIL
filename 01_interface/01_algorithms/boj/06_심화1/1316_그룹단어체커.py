# https://www.acmicpc.net/problem/1316
N = int(input())
total = 0

for _ in range(N):
    S = input()
    is_group = True

    for i, s in enumerate(S[:-1]):
        for j in range(i+2, len(S)):
            if s != S[j-1] and s == S[j]:
                is_group = False
                break

        if not is_group:
            break

    if is_group:
        total += 1

print(total)
