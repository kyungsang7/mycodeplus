from collections import deque

S = list(input())
T = list(input())

ans = 0

while T:
    if S == T:
        ans = 1
        break

    alp = T.pop()

    if alp == 'B':
        T = T[::-1]

print(ans)