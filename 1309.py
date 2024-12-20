count = [[0,0,0] for _ in range(10**5+1)]
count[1] = [1,1,1]
for i in range(2,10**5+1):
    count[i][0] = (count[i-1][1] + count[i-1][2]) % 9901
    count[i][1] = (count[i-1][0] + count[i-1][2]) % 9901
    count[i][2] = (count[i-1][0] + count[i-1][1] + count[i-1][2]) % 9901
print(sum(count[int(input())]) % 9901)