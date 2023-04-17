# https://www.acmicpc.net/problem/11021
import sys

T = int(sys.stdin.readline().rstrip())

for t in range(1, T+1):
    A, B = list(map(int, sys.stdin.readline().rstrip().split()))
    print(f'Case #{t}: {A + B}')
