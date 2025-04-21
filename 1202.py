import heapq

N, K = map(int,input().split())

jewels = []
for _ in range(N):
    jewels.append(tuple(map(int,input().split())))
jewels.sort(reverse=True)

bags = []
for _ in range(K):
    bags.append(int(input()))
bags.sort(reverse=True)

heap = []
ans = 0

while bags:
    bag = bags.pop()

    while jewels:
        weight, value = jewels.pop()
        if weight > bag:
            jewels.append((weight, value))
            break
        
        heapq.heappush(heap, -value)
    
    if heap:
        ans -= heapq.heappop(heap)

print(ans)