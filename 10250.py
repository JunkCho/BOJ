T = int(input())
for i in range(T):
    H,W,N = map(int,input().split())
    if N % H == 0:
        B = N//H
        if B < 10 :
            print(str(H)+'0'+str(B))
        else : print(str(H)+str(B))
        
    else :
        F = N%H
        B = (N // H)+ 1
        if B < 10 :
            print(str(F)+'0'+str(B))
        else : print(str(F)+str(B))
