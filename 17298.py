N = int(input())
line = list(map(int,input().split()))
stack = []
ans = [-1] * N

for i in range(N):
    while stack and line[stack[-1]] < line[i]:
        ans[stack.pop()] = line[i]
    stack.append(i)
print(*ans)