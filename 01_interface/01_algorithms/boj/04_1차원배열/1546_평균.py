# https://www.acmicpc.net/problem/1546
N = int(input())
rates = list(map(int, input().split()))
print(sum(rates) * 100 / (max(rates) * N))
