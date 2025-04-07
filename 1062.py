from itertools import combinations

def make_bit(word):
    bit = 0
    for i in word:
        bit = bit | 1 << (ord(i) - 97)
    
    return bit

N, K = map(int,input().split())
alps = set()
words_bit = []
ans = 0

for i in range(N):
    word = input()
    words_bit.append(make_bit(word))
    alps.update(word)

base_bit = make_bit('antic')

if K < 5:
    print(0)
else:


    for combination in combinations([1 << i for i in range(26) if not 1 << i & base_bit], K - 5):
        bit = sum(combination) | base_bit
        count = 0
        for i in words_bit:
            if bit & i == i:
                count += 1
        
        ans = max(ans, count)
    print(ans)