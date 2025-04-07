from collections import deque
import sys

input = sys.stdin.readline

def make(a, b):
    return 2 * min(a, b), max(a, b) - min(a, b)

A, B, C = map(int, input().split())
queue = deque([(A, B, C)])
visited = set()  # 리스트 대신 집합(set) 사용

while queue:
    a, b, c = queue.popleft()
    
    # 현재 상태를 집합으로 변환하여 방문 여부 확인
    current_state = tuple(sorted([a, b, c]))
    if current_state in visited:
        continue
    
    visited.add(current_state)  # 방문 기록 저장

    # 종료 조건
    if a == b == c:
        print(1)
        break

    # 새로운 상태 생성
    a1, b1 = make(a, b)
    queue.append((a1, b1, c))

    a1, c1 = make(a, c)
    queue.append((a1, b, c1))

    b1, c1 = make(b, c)
    queue.append((a, b1, c1))

else:
    print(0)