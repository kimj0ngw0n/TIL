# https://www.acmicpc.net/problem/10818
N = int(input())
nums = list(map(int, input().split()))

min_num = max_num = nums[0]

for num in nums:
    if min_num > num:
        min_num = num
    if max_num < num:
        max_num = num

print(f'{min_num} {max_num}')
