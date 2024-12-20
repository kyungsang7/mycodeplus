nums = [0] * (10**6+1)
nums[1], nums[2], nums[3] = 1, 2, 4
for i in range(4,10**6+1):
    nums[i] = (nums[i-1] + nums[i-2] + nums[i-3]) % (10**9+9)
for _ in range(int(input())):
    print(nums[int(input())] % (10**9+9))