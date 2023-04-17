# https://www.acmicpc.net/problem/2439
import sys

N = int(sys.stdin.readline().rstrip())

for n in range(1, N+1):
    print(' ' * (N - n) + '*' * n)
