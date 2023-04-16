# https://www.acmicpc.net/problem/24265
'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 1
        for j <- i + 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}
'''

n = int(input())

print(sum(list(range(2, n+1))) - (n - 1))
print(2)
