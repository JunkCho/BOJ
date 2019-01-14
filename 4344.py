A  = int(input())
for i in range(A):
    B = list(map(int, input().split()))
    count =0
    temp =0
    for j in range(1,B[0]+1):
        temp += B[j]
        temp/B[0]
    for k in range(1, B[0]+1):    
        if B[k] > temp/B[0]:
            count += 1
        else :
            pass
    print('%.3f%%' %(count/B[0]*100))
