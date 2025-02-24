import copy, sys
sys.setrecursionlimit(10 ** 5)

def making_cycle_DFS(num, count):
    global cycle_map, node

    if count >= 3 and num == node:
        cycle_map = copy.deepcopy(visited)
        return
    
    for next_node in adj_list[num]:
        if not visited[next_node]:
            visited[next_node] = True
            making_cycle_DFS(next_node, count + 1)
            visited[next_node] = False

def distance_DFS(node, count):
    global ans
    if cycle_map[node]:
        ans = count
        return
    
    
    for next_node in adj_list[node]:
        if not visited[next_node]:
            visited[next_node] = True
            distance_DFS(next_node, count + 1)
            visited[next_node] = False

N = int(input())
visited, cycle_map = [False] * (N + 1), []
adj_list = list(list() for _ in range(N + 1))

for _ in range(N):
    a,b = map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

for i in range(1, N + 1):
    if cycle_map:
        continue
    node = i
    making_cycle_DFS(i, 0)

for n in range(1, N + 1):
    ans = 0
    visited[n] = True
    distance_DFS(n, 0)
    visited[n] = False
    print(ans, end=' ')
