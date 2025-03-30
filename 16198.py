def DFS(count):
    global ans, recent
    if count == N - 2:
        ans = max(ans, recent)
        return

    for i in range(1, N - 1):
        if not visited[i]:
            visited[i] = True
            for j in range(i, -1, -1):
                if not visited[j]:
                    right = j
                    break
            for j in range(i, N):
                if not visited[j]:
                    left = j
                    break
            energy = nums[right] * nums[left]
            recent += energy
            DFS(count + 1)
            visited[i] = False
            recent -= energy

N = int(input())
nums = list(map(int,input().split()))
visited = [False] * N

ans = 0
recent = 0

DFS(0)

print(ans)
