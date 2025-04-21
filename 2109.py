N = int(input())

course = []
for i in range(N):
    course.append(list(map(int,input().split())))
course.sort(key = lambda x: (-x[0], -x[0]))

visited = [False] * (10 ** 4 + 1)
ans = 0

for money, deadline in course:
    for i in range(deadline, 0, -1):
        if not visited[i]:
            ans += money
            visited[i] = True
            break

print(ans)
