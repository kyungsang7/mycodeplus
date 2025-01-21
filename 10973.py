N = int(input())
nums = list(map(int,input().split()))
x, y = -1, -1

for i in range(N-1, 0, -1):
    if nums[i] < nums[i - 1]:
        x, y = i - 1, i
        break

for i in range(N - 1, x, -1):
    if nums[x] > nums[i]:
        nums[x], nums[i] = nums[i], nums[x]
        break

if x == y == -1:
    print(-1)
else:
    print(*nums[:y] + sorted(nums[y:], reverse = True))