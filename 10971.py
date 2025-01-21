N = int(input())
dist = list(list(map(int,input().split())) for _ in range(N))

visited = []
ans = 10 ** 7 + 1
def DFS():
    global visited, ans
    if len(visited) == N:
        res = 0
        for i in range(N - 1, -1, -1):
            if dist[visited[i - 1]][visited[i]] == 0:
                return
            res += dist[visited[i - 1]][visited[i]]
        ans = min(ans, res)
        return
    
    for i in range(N):
        if not i in visited:
            visited.append(i)
            DFS()
            visited.pop()

DFS()

print(ans)