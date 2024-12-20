nums = [[0] * 201 for _ in range(201)]
nums[0][0] = 1
for i in range(1,201):
    for j in range(201):
        nums[i][j] = nums[i][j-1] + nums[i-1][j]
N,K = map(int,input().split())
print(nums[K][N] % (10**9))