from collections import deque

def BFS():
    global visited, count

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            n_x, n_y = x + x_list[i], y + y_list[i]
            if 0 <= n_x < N and 0 <= n_y < N and not visited[n_x][n_y] and complex_map[n_x][n_y]:
                count += 1
                visited[n_x][n_y] = True
                queue.append((n_x, n_y))


x_list, y_list = [0,0,1,-1], [1,-1,0,0]

N = int(input())
complex_map, visited, ans = [], list([False] * N for _ in range(N)), []

for i in range(N):
    complex_map.append(list(map(int,input())))

for i in range(N):
    for j in range(N):
        if not visited[i][j] and complex_map[i][j]:
            visited[i][j] = True
            queue = deque([(i,j)])
            count = 1
            BFS()
            ans.append(count)

print(len(ans))
for i in sorted(ans):
    print(i)