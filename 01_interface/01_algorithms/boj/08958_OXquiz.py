# https://www.acmicpc.net/problem/8958

T = int(input())

for _ in range(T):
    ox = input()
    result = 0
    tmp = 0

    for i in range(len(ox)):
        if ox[i] == 'X':
            tmp = 0
        else:
            tmp += 1
            result += tmp

    print(result)
