nums = [True] * (10**6+1)
nums[1]= False

for i in range(2,10**6+1):
    if nums[i]:
        for j in range(i+i, 10**6+1, i):
            nums[j] = False
ans = 0
a,b = map(int,input().split())
for i in range(a,b+1):
    if nums[i]: print(i)
