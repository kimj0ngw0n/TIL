# https://www.acmicpc.net/problem/25501
def recursion(s, count):
    count += 1

    if len(s) == 1 or len(s) == 0:
        return [1, count]
    else:
        if s[0] != s[-1]:
            return [0, count]
        else:
            return recursion(s[1:-1], count)


def isPalindrome(s):
    return recursion(s, 0)


T = int(input())
for t in range(T):
    s = input()

    result = isPalindrome(s)

    print(f'{result[0]} {result[1]}')
