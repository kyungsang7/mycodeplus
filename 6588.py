prime = [True]*(10**6+1)
for i in range(2,10**6+1):
    if prime[i]:
        for j in range(i+i,10**6+1,i):
            prime[j] = False
while True:
    num = int(input())
    if num == 0:
        break
    for i in range(2,num):
        if prime[i] and prime[abs(i-num)]:
            print(num,'=',i,'+',abs(i-num))
            break
    else:
        print( "Goldbach's conjecture is wrong.")
        