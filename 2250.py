def DFS(node, depth):
    global count
    first_num = tree[node][0]
    second_num = tree[node][1]

    if first_num != -1:
        DFS(first_num, depth + 1)
    
    counting_list[node] = count
    max_length[depth] = max(max_length[depth], count)
    min_length[depth] = min(min_length[depth], count)
    count += 1

    if second_num != -1:
        DFS(second_num, depth + 1)

N = int(input())
count = 1
counting_list = [0] * (N + 1)
visited = [False] * (N + 2)
tree = dict()
max_length, min_length = [0] * 10001, [10000] * 10001


for i in range(N):
    a, b, c = map(int,input().split())
    visited[b], visited[c] = True, True
    tree[a] = (b, c)

for i in range(1, N + 1):
    if not visited[i]:
        leap = i
        break

DFS(leap, 1)

max_num = 0
max_idx = 0
idx = 1

for i in range(1, 10000):

    if max_num < max_length[i] - min_length[i] + 1:
        max_num = max_length[i] - min_length[i] + 1
        max_idx = idx

    idx += 1

print(max_idx, max_num)