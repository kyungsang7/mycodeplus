from collections import deque

x_list, y_list = [0, 0, 1, -1], [-1, 1, 0, 0]

def make_map(i, j):
    queue = deque([(i, j)])
    coun = 0

    while queue:
        x, y = queue.popleft()
        if wall_map[x][y] == 1 or island_map[x][y] != 0:
            continue

        coun += 1
        island_map[x][y] = island_num

        for i in range(4):
            nx, ny = x + x_list[i], y + y_list[i]
            if  0 <= nx < N and 0 <= ny < M:
                queue.append((nx, ny))
    
    return coun


N, M = map(int,input().split())
wall_map = list(list(map(int,input())) for _ in range(N))
island_num = 2

island_dict = dict()
island_dict[0] = 0
island_map = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if wall_map[i][j] == island_map[i][j] == 0:
            island_dict[island_num] = make_map(i, j)
            island_num += 1

for i in range(N):
    for j in range(M):
        if wall_map[i][j] == 1:
            islands = set()
            for s in range(4):
                ni, nj = i + x_list[s], j + y_list[s]
                if 0 <= ni < N and 0 <= nj < M:
                    islands.add(island_map[ni][nj])

            for s in islands:
                wall_map[i][j] += island_dict[s]
            
            wall_map[i][j] %= 10


for i in wall_map:
    print(''.join(map(str, i)))
