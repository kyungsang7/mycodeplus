nums = [0,1,2,4] + [0] * 997
for i in range(4,1001):
    nums[i] = nums[i-1] + nums[i-2] + nums[i-3]
for _ in range(int(input())):
    print(nums[int(input())])