N = int(input())
nums = list(map(int,input().split()))
res = [0] * N
res[0] = nums[0]

for i in range(1,N):
    res[i] = nums[i]
    for j in range(i):
        if nums[i] > nums[j]:
            res[i] = max(res[i], res[j] + nums[i])
print(max(res))