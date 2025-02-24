import sys
sys.setrecursionlimit(10 ** 5)

def DFS(node):
    global ans, nodes, visited
    visited[node] = True

    for next_node in adj_list[node]:
        if not visited[next_node]:
            visited[next_node] = True
            nodes[next_node] = (nodes[node] + 1) % 2
            DFS(next_node)
        else:
            if nodes[node] == nodes[next_node]:
                ans = "NO"
                return

for _ in range(int(input())):
    V, E = map(int,input().split())
    
    adj_list = list(list() for _ in range(V + 1))
    visited = [False] * (V + 1)
    nodes = [0] * (V + 1)
    ans = "YES"

    for _ in range(E):
        a,b = map(int,input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)

    for i in range(1, V + 1):
        if ans == "NO" or visited[i]:
            continue
    
        DFS(i)
    
    print(ans)


