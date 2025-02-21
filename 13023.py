def DFS(node, count):
    global visited, ans

    if ans:
        return
    
    if count == 5:
        ans = 1
        return

    for next_node in adj_list[node]:
        if not visited[next_node]:
            visited[next_node] = True
            DFS(next_node, count + 1)
            visited[next_node] = False

N,M = map(int,input().split())

adj_list = list(list() for _ in range(N))
ans = 0
visited = [False] * N

#인접리스트 생성
for i in range(M):
    a,b = map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

for i in range(N):
    visited[i] = True
    DFS(i, 1)
    visited[i] = False

print(ans)