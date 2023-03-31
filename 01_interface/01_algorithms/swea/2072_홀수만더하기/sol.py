# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QSEhaA5sDFAUq

import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(T):
    total = 0
    numbers = map(int, input().split())

    for num in numbers:
        if num % 2:
            total += num

    print(f'#{tc+1} {total}')
