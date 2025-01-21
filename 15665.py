a,b = map(int,input().split())
nums = sorted(set(list(map(int,input().split()))))

ans = []

def DFS():
    global ans
    if len(ans) == b:
        print(*ans)
        return
    
    for i in range(len(nums)):
        ans.append(nums[i])
        DFS()
        ans.pop()

DFS()

