L_stack= list(input())
D_stack = []

for i in range(int(input())):
    command = list(input().split())
    if command[0] == 'L':
        if L_stack:
            D_stack.append(L_stack.pop())
    elif command[0] == 'D':
        if D_stack:
            L_stack.append(D_stack.pop())
    elif command[0] == 'B':
        if L_stack:
            L_stack.pop()
    else:
        L_stack.append(command[1])
        
for i in L_stack+D_stack[::-1]:
    print(i,end='')