N,S = map(int,input().split())
nums = list(map(int,input().split()))
ans = 0

def back(num):
    global ans
    if len(res) == target:
        if sum(res) == S:
            ans += 1
        return
    
    for i in range(num, N):
        res.append(nums[i])
        back(i + 1)
        res.pop()

for i in range(1, N + 1):
    res = []
    target = i
    back(0)

print(ans)