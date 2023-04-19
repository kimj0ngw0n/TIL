# https://www.acmicpc.net/problem/2908
A, B = input().split()
a = b = ''

for i in range(2, -1, -1):
    a += A[i]
    b += B[i]

a = int(a)
b = int(b)

print(a if a > b else b)
