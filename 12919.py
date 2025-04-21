from collections import deque

S = input()
T = input()

queue = deque([T])

while queue:    
    word = queue.popleft()

    if len(word) < len(S):
        break

    if word == S:
        print(1)
        exit()
    
    if word[0] == 'B':
        queue.append(word[1:][::-1])
    
    if word[-1] == 'A':
        queue.append(word[:-1])

print(0)