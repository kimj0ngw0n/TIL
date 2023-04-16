# https://www.acmicpc.net/problem/24264
'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}
'''


n = int(input())

print(n * n)
print(2)
