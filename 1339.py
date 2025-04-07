def calculate():
    res = 0
    for word in words:
        word_lenght = len(word)
        for i in range(word_lenght):
            res += alp[word[i]] * 10 ** (word_lenght - i - 1)
    
    return res

N = int(input())
words, alp = list(), dict()
ans = 0

for _ in range(N):
    word = input()
    words.append(word)

    for i in range(len(word)):
        if word[i] in alp:
            alp[word[i]] += 10 ** (len(word) - i - 1)
        else:
            alp[word[i]] = 10 ** (len(word) - i - 1)

alp = sorted(alp.items(), key=lambda x: -x[1])
ans = 0

for i in range(len(alp)):
    ans += alp[i][1] * (9 - i)

print(ans)