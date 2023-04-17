# https://www.acmicpc.net/problem/2480
dices = list(map(int, input().split()))

same = [
    dices[0] == dices[1],
    dices[1] == dices[2],
    dices[2] == dices[0],
    ]

if sum(same) == 3:
    print(10000 + dices[0] * 1000)
elif sum(same) == 1:
    if same[0] or same[1]:
        print(1000 + dices[1] * 100)
    else:
        print(1000 + dices[0] * 100)
else:
    print(max(dices) * 100)
