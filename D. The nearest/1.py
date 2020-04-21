input()
nums, N = input().split(), int(input())
for i, num in enumerate(nums):
    nums[i] = int(num)
difference, current_idx = abs(N - nums[0]), 0

for i in range(1, len(nums)):
    if difference > abs(N - nums[i]):
        difference, current_idx = abs(N - nums[i]), i
print(nums[current_idx])
