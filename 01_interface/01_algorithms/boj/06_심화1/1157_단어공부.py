# https://www.acmicpc.net/problem/1157
A = [0 for _ in range(26)]
S = input()

for s in S:
    if ord(s) > 96:
        A[ord(s)-97] += 1
    else:
        A[ord(s)-65] += 1

m = max(A)
m_idx = A.index(m)
A.remove(m)
m1 = max(A)
if m == m1:
    print('?')
else:
    print(chr(65+m_idx))
