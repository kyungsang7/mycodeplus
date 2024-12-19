nums = [[0] * 10 for _ in range(101)]
nums[1] = [0,1,1,1,1,1,1,1,1,1]
for i in range(2,101):
    for j in range(10):
        if j - 1 >= 0:
            nums[i][j] += nums[i-1][j-1]
        if j + 1 <= 9:
            nums[i][j] += nums[i-1][j+1]
        nums[i][j] = nums[i][j] % 1000000000
print(sum(nums[int(input())]) % 1000000000)
