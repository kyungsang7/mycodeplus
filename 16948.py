from collections import deque

r_list, c_list = [-2, -2, 0, 0, 2, 2], [-1, 1, -2, 2, -1, 1]

N = int(input())
r1, c1, r2, c2 = map(int,input().split())

queue = deque([(r1, c1, 0)])
visited = [(r1, c1)]
ans = -1

while queue:
    r, c, count = queue.popleft()
    if r == r2 and c == c2:
        ans = count
        break

    for i in range(6):
        nr, nc = r + r_list[i], c + c_list[i]
        if 0 <= nr < N and 0 <= nc < N and not (nr, nc) in visited:
            visited.append((nr, nc))
            queue.append((nr, nc, count + 1))

print(ans)