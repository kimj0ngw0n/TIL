# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVF-WqqecDFAWg

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())

    colors = []
    for _ in range(N):
        colors.append(list(map(int, input().split())))

    matrix = [[0 for _ in range(10)] for _ in range(10)]

    # 모든 색칠에 대해
    for color in colors:
        # 색칠 한줄씩 실행
        for row in range(color[0], color[2]+1):
            for col in range(color[1], color[3]+1):
                if matrix[row][col] != 3 and color[4] != matrix[row][col]:
                    matrix[row][col] += color[4]

    total = 0
    for row in matrix:
        total += row.count(3)

    print(f'#{t} {total}')
