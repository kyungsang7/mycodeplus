def DFS(num):
    visited[num] = True
    for i in adj_list[num]:
        if not visited[i]:
            DFS(i)

N, M = map(int,input().split())
visited = [False] * (N + 1)
ans = 0

#인접리스트 만들기
adj_list = list(list() for _ in range(N + 1))
for i in range(M):
    a,b = map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

for i in range(1, N + 1):
    if not visited[i]:
        DFS(i)
        ans += 1

print(ans)