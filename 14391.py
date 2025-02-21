N, M = map(int,input().split())
nums = list(input() for _ in range(N))
ans = 0

ans = 0
for i in range(N):
    ans += int(nums[i])

res = 0
for i in range(M):
    deg = 0
    for j in range(N - 1, -1, -1):
        res += int(nums[j][i]) * (10 ** deg)
        deg += 1

print(max(ans, res))
