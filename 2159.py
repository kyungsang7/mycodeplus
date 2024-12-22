N = int(int(input()))
nums = [int(input()) for _ in range(N)] + [0] * 3
ans = [0] * (N+3) 
for i in range(N):
    ans[i] = max(ans[i-1], ans[i-2] + nums[i], nums[i] + nums[i-1] + ans[i-3])
print(ans[N-1])
print(ans)