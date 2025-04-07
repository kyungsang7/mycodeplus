visited = [0] * (2000001)
N = int(input())
S = list(map(int,input().split()))

for i in range(1 << N):
    print(i)
    num = 0
    for j in range(N):
        if i & (1 << j):
            num += S[j]
    visited[num] = 1

for i in range(1, 2000001):
    if visited[i] == 0:
        print(i)
        break