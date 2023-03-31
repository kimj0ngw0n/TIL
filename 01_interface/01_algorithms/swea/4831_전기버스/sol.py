# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVFCzaqeUDFAWg#

import sys
sys.stdin = open('sample_input.txt')


T = int(input())

for t in range(T):
    K, N, M = list(map(int, input().split()))
    station_number = list(map(int, input().split()))

    total = prev = 0
    station = ['' for _ in range(N+1)]
    for i in station_number:
        station[i] = 'O'

    while K + prev < N:
        box_station = station[prev+1:prev+K+1]
        if 'O' in box_station:
            total += 1
            box_station.reverse()
            prev += len(box_station)-box_station.index('O')
        else:
            total = 0
            break

    print(f'#{t+1} {total}')
