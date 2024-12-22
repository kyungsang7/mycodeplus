from collections import deque
queue = deque()

def BFS(num):
    ind = 1
    queue.append(num)
    while queue:
        node = queue.popleft()
        if visited[node]:
            continue
        visited[node] = True
        ans[node] = ind
        ind += 1
        for next_node in adj_list[node]:
            if not visited[next_node]:
                queue.append(next_node)

N,M,R = map(int,input().split())
adj_list = [[] for _ in range(N+1)]
visited = [False] * (N+1)
ans = [0] * (N+1)

for _ in range(M):
    a,b = map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)
for i in adj_list:
    i = i.sort(reverse=True)
BFS(R)
for i in ans[1:]:
    print(i)