from collections import deque

def simulation():
    durability.appendleft(durability.pop())
    robots.appendleft(robots.pop())

    robots[N - 1] = 0

    for i in range(2 * N - 2, -1, -1):
        if robots[i] == 1 and robots[i + 1] == 0:
            if durability[i + 1] > 0:
                durability[i + 1] -= 1
                robots[i + 1] = 1
                robots[i] = 0
    
    robots[N - 1] = 0

    if durability[0] > 0:
        durability[0] -= 1
        robots[0] = 1

    if durability.count(0) >= K:
        return True
    return False


N, K = map(int,input().split())
durability = deque(list(map(int,input().split())))
robots = deque([0] * 2 * N)
ans = 0

while True:
    ans  += 1
    if simulation():
        print(ans)
        break

