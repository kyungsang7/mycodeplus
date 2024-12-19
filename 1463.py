N = int(input())
nums = [10**6] * (N+1)
nums[N] = 0
for i in range(N,1,-1):
    if i % 3 == 0:
        nums[i//3] = min(nums[i]+1, nums[i//3])
    if i % 2 == 0:
        nums[i//2] = min(nums[i]+1, nums[i//2])
    nums[i-1] = min(nums[i-1],nums[i]+1)
print(nums[1])