L, C = map(int,input().split())
alphs = sorted(list(input().split()))

password = []
vowels = ['a', 'e', 'i', 'o', 'u']

def Recursive_call(num):
    global password
    if len(password) == L:
        v, c = 0, 0
        for i in password:
            if i in vowels:
                v += 1
            else:
                c += 1

        if 1 <= v and 2 <= c:
            print(''.join(password))

        return
    
    for i in range(num, C):
        if not alphs[i] in password:
            password.append(alphs[i])
            Recursive_call(i + 1)
            password.pop()

Recursive_call(0)