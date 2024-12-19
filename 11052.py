num = int(input())
nums = [0] + list(map(int,input().split()))

for i in range(1,num+1):
    for j in range(1,i):
        nums[i]= max(nums[j] + nums[i-j], nums[i])
        
print(nums[-1])