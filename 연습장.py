nums = {}

int(input())
for i in list(map(int,input().split())):
    if i in nums:
        nums[i] += 1    
    else:
        nums[i] = 1

int(input())
for i in list(map(int,input().split())):
    if i in nums:
        print(nums[i], end = ' ')
    
    else:
        print(0, end = ' ')