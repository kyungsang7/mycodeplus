import sys, copy

def find(num):
    nums_copy = copy.deepcopy(nums)

    for i in range(3):
        if i != num:
            nums_copy[0][i] = sys.maxsize
    
    for i in range(1, N):
        nums_copy[i][0] += min(nums_copy[i-1][1], nums_copy[i-1][2])
        nums_copy[i][1] += min(nums_copy[i-1][0], nums_copy[i-1][2])
        nums_copy[i][2] += min(nums_copy[i-1][0], nums_copy[i-1][1])
    
    if num == 0:
        return min(nums_copy[-1][1], nums_copy[-1][2])
    elif num == 1:
        return min(nums_copy[-1][0], nums_copy[-1][2])
    else:
        return min(nums_copy[-1][0], nums_copy[-1][1])


N = int(input())
nums = [list(map(int,input().split())) for _ in range(N)]
ans = sys.maxsize

for i in range(3):
    ans = min(ans, find(i))

print(ans)