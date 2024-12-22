N = int(input())
nums = [list(map(int,input().split())) for _ in range(N)]
ans = [[0] * i for i in range(1, N+1)]
ans[0][0] = nums[0][0]
for i in range(1,N):
    for j in range(i//2+1):
        if j == 0:
            ans[i][j] = ans[i-1][j] + nums[i][j]
            ans[i][i-j] = ans[i-1][i-j-1] + nums[i][i-j]
        else:
            ans[i][j] = max(ans[i-1][j] + nums[i][j], ans[i-1][j-1] + nums[i][j])
            ans[i][i-j] = max(ans[i-1][i-j] + nums[i][i-j], ans[i-1][i-j-1] + nums[i][i-j])
print(max(ans[-1]))