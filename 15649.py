a,b = map(int,input().split())
ans = []

def DFS():
    global ans

    if len(ans) == b:
        print(*ans)
        return
    
    for i in range(1, a + 1):
        if not i in ans:
            ans.append(i)
            DFS()
            ans.pop()
DFS()