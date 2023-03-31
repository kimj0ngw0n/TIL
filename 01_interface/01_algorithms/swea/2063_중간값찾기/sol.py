# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QPsXKA2UDFAUq

import sys
sys.stdin = open('input.txt')

N = int(input())
result = 0

numbers = list(map(int, input().split()))
numbers.sort()
result = numbers[N // 2]

print(result)
