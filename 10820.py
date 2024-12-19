while True:
    try:
        a = input()
        b,c,d,e = 0 ,0 ,0 ,0
        for i in a:
            if 48 <= ord(i) <= 57: d+=1
            elif 65 <= ord(i) <= 90: c+=1
            elif 97 <= ord(i) <= 122: b+=1
            else: e+=1
        print(b,c,d,e)
    except EOFError:
        break