a,b = map(int,input().split())
nums = sorted(list(map(int,input().split())))
ans = []

def DFS():
    global ans

    if len(ans) == b:
        print(*ans)
        return
    
    for i in range(len(nums)):
        if not nums[i] in ans:
            ans.append(nums[i])
            DFS()
            ans.pop()
DFS()