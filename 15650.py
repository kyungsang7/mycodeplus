a,b = map(int,input().split())
ans = []

def DFS(num):
    global ans

    if len(ans) == b:
        print(*ans)
        return
    
    for i in range(num, a + 1):
        if not i in ans:
            ans.append(i)
            DFS(i)
            ans.pop()
DFS(1)