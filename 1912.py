num = int(input())
nums = [0] + list(map(int,input().split()))
ans = [0] * (num + 1)

for i in range(1,num + 1):
    ans[i] = max(ans[i-1] + nums[i], nums[i])

print(max(ans[1:]))