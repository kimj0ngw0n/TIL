# https://www.acmicpc.net/problem/24060

def merge(A, p, q, r, k, K):
    tmp = []
    i = p
    j = q + 1
    t = 0

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    while i <= q:
        tmp.append(A[i])
        i += 1

    while j <= r:
        tmp.append(A[j])
        j += 1

    i = p
    while i <= r:
        A[i] = tmp[t]

        if k == K:
            print(tmp[t])
        k += 1
        i += 1
        t += 1

    return k


def merge_sort(A, p, r, k, K):
    if p < r:
        q = (p + r) // 2
        k = merge_sort(A, p, q, k, K)
        k = merge_sort(A, q + 1, r, k, K)
        k = merge(A, p, q, r, k, K)

    return k


N, K = map(int, input().split())
A = list(map(int, input().split()))
k = 1

k = merge_sort(A, 0, len(A)-1, k, K) - 1

if k < K:
    print(-1)
