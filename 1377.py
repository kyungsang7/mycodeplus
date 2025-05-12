N = int(input())
A = []

for i in range(N):
    num = int(input())
    A.append((num, i))

A_sorted = sorted(A)
ans = -float('inf')

for i in range(N):
    ans = max(ans, A_sorted[i][1] - A[i][1])

print(ans + 1)