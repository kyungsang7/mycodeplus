square_list = [10**5] * (10**5+1)
square_list[1] = 1
for i in range(2,10**5+1):
    if (i ** 0.5) % 1 == 0:
        square_list[i] = 1
        continue
    for j in range(1,i):
        square_list[i] = min(square_list[i], square_list[j] + square_list[i-j])
print(square_list[int(input())])