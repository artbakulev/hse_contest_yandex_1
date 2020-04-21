input()
nums = list(map(int, input().split()))
N = int(input())

diff, diff_idx = abs(N - nums[0]), 0

for i in range(1, len(nums)):
    if abs(N - nums[i]) < diff:
        diff = abs(N - nums[i])
        diff_idx = i
print(nums[diff_idx])
