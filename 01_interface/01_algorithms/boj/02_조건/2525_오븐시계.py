# https://www.acmicpc.net/problem/2525
A, B = list(map(int, input().split()))
C = int(input())

CH = C // 60
CM = C % 60

B += CM
if B >= 60:
    B -= 60
    A += 1

A += CH
if A >= 24:
    A -= 24

print(f'{A} {B}')
