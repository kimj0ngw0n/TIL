# https://www.acmicpc.net/problem/3052
nums = []
for _ in range(10):
    nums.append(int(input()))

result = set()
for i in range(10):
    result.add(nums[i] % 42)

print(len(result))
