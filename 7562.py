from collections import deque

def BFS():
    while queue:
        x, y = queue.popleft()

        if x == goal[0] and y == goal[1]:
            return night_map[x][y]

        for i in range(8):
            nx, ny = x + x_list[i], y + y_list[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not night_map[nx][ny] or night_map[nx][ny] > night_map[x][y] + 1:
                    night_map[nx][ny] = night_map[x][y] + 1
                    queue.append((nx, ny))

x_list, y_list = [2, 2, 1, 1 , -1, -1, -2, -2], [1, -1, 2, -2, 2, -2, 1, -1]

for _ in range(int(input())):
    N = int(input())
    night_map = list([0] * N for _ in range(N))
    queue = deque()
    queue.append(tuple(map(int,input().split())))
    goal = tuple(map(int,input().split()))
    print(BFS())
