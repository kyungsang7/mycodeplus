N = int(input())
nums = list(map(int,input().split()))

forward = [1] * N
backward = [1] * N

for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            forward[i] = max(forward[i], forward[j] + 1)
    for j in range(N-1, N-i-1, -1):
        if nums[N-i-1] > nums[j]:
            backward[N-i-1] = max(backward[N-i-1], backward[j] + 1)
ans = 0
for i in range(N):
    ans = max(ans, forward[i] + backward[i])
print(ans-1)
