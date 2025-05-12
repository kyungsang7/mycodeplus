def bin(num):
    idx = nums[0]
    wifi = 1

    for i in range(1, len(nums)):
        if nums[i] - idx >= num:
            wifi += 1
            idx = nums[i]
        
    return wifi

N, C = map(int,input().split())
nums = sorted(list(int(input()) for _ in range(N)))
left, right = 0, 10 ** 9

while left <= right:
    mid = (left + right) // 2
    res = bin(mid)

    if res >= C:
        left = mid + 1
    
    else:
        right = mid - 1

print(right)