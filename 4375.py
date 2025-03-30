while True:
    try:
        N = int(input())
    except:
        break

    num = 1
    count = 1
    while True:
        if int(num) % N == 0:
            print(count)
            break

        num = num * 10 + 1
        count += 1