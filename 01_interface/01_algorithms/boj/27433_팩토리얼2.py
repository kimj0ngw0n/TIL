# https://www.acmicpc.net/problem/27433

N = int(input())


def fac(n):
    if n == 0:
        return 1

    return n * fac(n - 1)


print(fac(N))
