def calculate():
    true_team, false_team = 0, 0
    for i in range(N):
        for j in range(N):
            if visited[i] == visited[j]:
                if visited[i]:
                    true_team += adj[i][j]
                else:
                    false_team += adj[i][j]
    
    return abs(true_team - false_team)

def get_nums(count, idx):
    global ans
    if count == N // 2:
        ans = min(ans, calculate())
        return
    
    for i in range(idx, N):
        visited[i] = True
        get_nums(count + 1, i + 1)
        visited[i] = False

N = int(input())
adj = list(list(map(int,input().split())) for _ in range(N))
visited = [False] * N
ans = float('inf')

get_nums(0, 0)

print(ans)