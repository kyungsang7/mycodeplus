def change_swich(nums, idx):
    for i in range(idx - 1, idx + 2):
        if 0 <= i < N:
            nums[i] = 1 - nums[i]

def get_nums(arr):
    nums = arr[:]
    ans = 0
    for i in range(N):
        if 0 < i < N:
            if nums[i - 1] != goal[i - 1]:
                ans += 1
                change_swich(nums, i)

    if nums == goal:
        return ans
    else:
        return float('inf')
    
N = int(input())
nums = list(map(int,input()))
goal = list(map(int,input()))

ans1 = get_nums(nums)

second_nums = nums[:]

change_swich(second_nums, 0)
ans2 = get_nums(second_nums) + 1

print(min(ans1, ans2) if not min(ans1, ans2) == float('inf') else -1)

