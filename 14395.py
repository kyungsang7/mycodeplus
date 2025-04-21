from collections import deque

a, b = map(int,input().split())
visited = set()
visited.add(a)
queue = deque([(a, '')])

if a == b:
    print(0)
    exit()

while queue:
    num, operator = queue.popleft()

    if num == b:
        print(operator)
        exit()

    for i in ['*', '+', '/']:
        if i == '*':
            nnum = num * num
            if nnum <= b and not nnum in visited:
                visited.add(nnum)
                queue.append((nnum, operator + '*'))

        elif i == '+':
            nnum = num + num
            if nnum <= b and not nnum in visited:
                visited.add(nnum)
                queue.append((nnum, operator + '+'))

        elif i == '/':
            nnum = 1
            if nnum <= b and not nnum in visited:
                visited.add(nnum)
                queue.append((nnum, operator + '/'))

print(-1)
