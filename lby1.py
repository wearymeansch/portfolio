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
ch1=int(input())
ch2=int(input())
ch3=int(input())
s=insert(None, ch1)
print(s)
s=insert(s, ch2)
print(s)
s=insert(s, ch3)
print(s)
