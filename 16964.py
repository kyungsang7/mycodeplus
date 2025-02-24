def make_parents(num):
    for i in adj_list[num]:
        if parents[i] == -1:
            parents[i] = num
            make_parents(i)


N = int(input())

adj_list = list(list() for _ in range(N + 1))
parents = [-1] * (N + 1)
parents[1] = 0
ans = 1

for _ in range(N - 1):
    a,b = map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

nums = list(map(int,input().split()))
make_parents(1)

for i in range(1, N):
    if parents[nums[i]] == parents[nums[i - 1]] or parents[nums[i]] == nums[i - 1]:
        continue
    else:
        ans = 0

print(ans)