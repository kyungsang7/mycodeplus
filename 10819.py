N = int(input())
nums = list(map(int,input().split()))
res = []
ans = 0
visited = [False] * N

def DFS():
    global ans, res, visited
    if len(res) == N:
        n_sum = 0
        for i in range(N - 1):
            n_sum += abs(res[i] - res[i + 1])
            ans = max(ans, n_sum)
        return
    
    for i in range(N):
        if not visited[i]:
            res.append(nums[i])
            visited[i] = True
            DFS()
            res.pop()
            visited[i] = False

DFS()

print(ans)
