# https://www.acmicpc.net/problem/4344
C = int(input())

for _ in range(C):
    S = list(map(int, input().split()))
    N = S[0]
    scores = S[1:]

    avg = sum(scores) / N
    print(f'{format(round(sum([avg < x for x in scores]) * 100 / N, 3), ".3f")}%')
