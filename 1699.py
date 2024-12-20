import sys
input = sys.stdin.readline

num = int(input())

square_list = [i for i in range(num+1)]

for i in range(2,num+1):
    for j in range(1,i):
        if i < j*j:
            break
        square_list[i] = min(square_list[i],square_list[i-j*j]+1)
print(square_list[num])
