from collections import deque
from copy import deepcopy

prime_list = [True] * 10000
for i in range(2, 5000):
    if prime_list[i]:
        for j in range(2, 5000):
            if i * j < 10000:
                prime_list[i * j] = False
            else:
                break

for _ in range(int(input())):
    prime = deepcopy(prime_list)
    num, goal = map(int,input().split())
    queue = deque([(num, 0)])
    ans = 'Impossible'

    while queue:
        n, count = queue.popleft()
        if n == goal:
            ans = count
            break

        prime[n] = False

        if n < 1000:
            continue

        for i in range(4):
            nnum = list(str(n))
            for j in range(10):
                nnum[i] = str(j)
                if prime[int(''.join(map(str, nnum)))]:
                    queue.append((int(''.join(map(str, nnum))), count + 1))

    print(ans)
