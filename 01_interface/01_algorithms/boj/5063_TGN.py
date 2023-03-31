# https://www.acmicpc.net/problem/5063

T = int(input())

for _ in range(T):
    future = list(map(int, input().split()))

    if future[0] < (future[1] - future[2]):
        print('advertise')
    elif future[0] > (future[1] - future[2]):
        print('do not advertise')
    else:
        print('does not matter')
