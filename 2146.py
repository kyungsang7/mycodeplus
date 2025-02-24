from collections import deque

x_list, y_list = [0, 0, 1, -1], [1, -1, 0, 0]

def BFS_island_map(x, y, island):
    queue = deque([(x, y)])
    island_map[x][y] = island
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + x_list[i], y + y_list[i]
            if 0 <= nx < N and 0 <= ny < N and island_map[nx][ny] == 1:
                island_map[nx][ny] = island
                queue.append((nx, ny))

def BFS_check_length(i, j):
    global ans
    queue = deque([(i, j, 0)])
    visited = set()
    island_name = island_map[i][j]
    
    while queue:
        x, y, dist = queue.popleft()
        for i in range(4):
            nx, ny = x + x_list[i], y + y_list[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                if island_map[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist + 1))
                elif island_map[nx][ny] != 0 and island_map[nx][ny] != island_name:
                    ans = min(ans, dist)
                    return

N = int(input())
island_map = [list(map(int, input().split())) for _ in range(N)]
island = 2
ans = float('inf')

for i in range(N):
    for j in range(N):
        if island_map[i][j] == 1:
            BFS_island_map(i, j, island)
            island += 1

for i in range(N):
    for j in range(N):
        if island_map[i][j] != 0:
            BFS_check_length(i, j)

print(ans)