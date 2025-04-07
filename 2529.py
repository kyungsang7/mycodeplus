def DFS(ope):
    global recent, visited
    if ope == k:
        ans.append(''.join(str(s) for s in recent))
        return
    
    for i in range(10):
        if not visited[i]:
            if operation[ope] == '>' and recent[-1] > i:
                recent.append(i)
                visited[i] = True
                DFS(ope + 1)
                recent.pop()
                visited[i] = False

            elif operation[ope] == '<' and recent[-1] < i:
                recent.append(i)
                visited[i] = True
                DFS(ope + 1)
                recent.pop()
                visited[i] = False



k = int(input())
operation = list(input().split())
ans = []

for i in range(10):
    recent = [i]
    visited = [False] * 10
    visited[i] = True
    DFS(0)
    
print(ans[-1])
print(ans[0])
