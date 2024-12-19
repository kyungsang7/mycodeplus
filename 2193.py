nums = [[0,0] for _ in range(91)]
nums[1] = [0,1]
for i in range(2,91):
    nums[i][0] = nums[i-1][0] + nums[i-1][1]
    nums[i][1] = nums[i-1][0]
print(sum(nums[int(input())]))