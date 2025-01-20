num = int(input())
borken_button = int(input())
if borken_button == 0:
    b_button = []
else:
    b_button = list(map(int,input().split()))

min_num = abs(100 - num) 

for i in range(10 ** 6 + 1):
    n = str(i)
    for j in range(len(n)):
        if int(n[j]) in b_button:
            break
        elif j == len(n) - 1:
            min_num = min(min_num, abs(num - i) + len(n))

print(min_num)