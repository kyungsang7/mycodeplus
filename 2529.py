import copy

N = int(input())
judge = list(input().split())

nums = []
ans = []
ans_min = []

def back_track():
    global nums, ans, ans_min
    if len(nums) == N + 1:
        for i in range(N):
            if judge[i] == '>':
                if not nums[i] > nums[i + 1]:
                    return
            else:
                if not nums[i] < nums[i + 1]:
                    return
        if not ans:
            ans_min = copy.deepcopy(nums)

        ans = copy.deepcopy(nums)
        return
    
    for i in range(10):
        if not i in nums:
            nums.append(i)
            back_track()
            nums.pop()

back_track()   
print(''.join(map(str, ans)))
print(''.join(map(str, ans_min)))