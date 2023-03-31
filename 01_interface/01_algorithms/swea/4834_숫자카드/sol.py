# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVFCzaqeUDFAWg#

import sys
sys.stdin = open('sample_input.txt')


T = int(input())

for t in range(1, T+1):
    N = int(input())
    ai = list(map(int, list(input())))
    counting = [0 for _ in range(10)]

    for i in range(len(counting)):
        counting[i] = ai.count(i)

    counting.reverse()
    big_number = counting.index(max(counting))

    print(f'#{t} {9 - big_number} {counting[big_number]}')
