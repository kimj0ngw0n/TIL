# https://www.acmicpc.net/problem/10870

def fib(n):
    if n == 0 or n == 1:
        return n

    return fib(n - 1) + fib(n - 2)


N = int(input())

print(fib(N))
