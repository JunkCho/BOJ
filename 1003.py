T = int(input())
i=m=n=0
for i in range(T):
    I = int(input())
    j=0
    if I == 0 :
        m=1
        n=0
        print(m, n)
    elif I == 1 :
        m=0
        n=1
        print(m,n)
    else :
        result1=0
        p1=0
        pp1=1
        p2= 1
        pp2= 0
        result2=0
        for j in range(I-1):
            result1 = p1 + pp1
            result2 = p2 + pp2
            pp1 = p1
            p1 = result1
            pp2 = p2
            p2 = result2
        print(result1, result2)
