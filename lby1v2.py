def insert(s,zn):
    if s == None:
        s=[zn, None]
    else:
        if zn>s[0]:
            if s[1]==None or s[1][0]>zn:
                s[1]=[zn, s[1]]
            else:
                s[1][1]=[zn, s[1][1]]
        else:
            s=[zn,s]
    return s
s=None
for i in range(4):
    ch1=int(input())
    s=insert(s, ch1)
    print(s)
