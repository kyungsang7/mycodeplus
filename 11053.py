num = int(input())
nums = list(map(int,input().split()))
ans = [1] * num

for i in range(1,num):
    for j in range(i):
        if nums[i] > nums[j]:
            ans[i] = max(ans[i], ans[j] + 1)

print(max(ans))