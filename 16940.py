from collections import deque

def making_children():
    queue = deque([1])
    
    while queue:
        node = queue.popleft()

        for i in adj_list[node]:
            if not visited[i]:
                visited[i] = True
                children_list[node].add(i)
                queue.append(i)


def BFS():
    global ans

    queue = deque([1])
    idx = 1

    while queue:
        node = queue.popleft()

        if set(nums[idx: idx + len(children_list[node])]) != children_list[node]:
            ans = 0
            return

        for i in nums[idx: idx + len(children_list[node])]:
            queue.append(i)
        
        idx += len(children_list[node])


N = int(input())
adj_list = list(list() for _ in range(N + 1))
children_list = list(set() for _ in range(N + 1))
visited = [False] * (N + 1)
visited[1] = True
ans = 1

for _ in range(N - 1):
    a,b = map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

nums = list(map(int,input().split()))

making_children()
BFS()

print(ans)