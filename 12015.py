def get_idx(num):
    left, right = 0, len(nums)

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == num:
            return mid
        
        elif nums[mid] < num:
            left = mid + 1
        
        else:
            right = mid - 1
    
    return left
        

N = int(input())
A = list(map(int,input().split()))

nums = [A[0]]

for i in A[1:]:
    if nums[-1] < i:
        nums.append(i)

    else:
        idx = get_idx(i)
        nums[idx] = i

print(len(nums))



