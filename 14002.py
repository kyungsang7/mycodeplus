num = int(input())
nums = list(map(int,input().split()))
counts = [1] * num
lines = [[0] for _ in range(num)]
for i in range(num):
    lines[i][0] = nums[i]
for i in range(1,num):
    for j in range(i):
        if nums[i] > nums[j]:
            if counts[i] < counts[j]+1:
                lines[i] = lines[j] + [nums[i]]
            counts[i] = max(counts[i], counts[j]+1)
print(max(counts))
print(*lines[counts.index(max(counts))])
