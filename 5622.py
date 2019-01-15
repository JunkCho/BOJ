A= input()
B = ['0','1','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
B[4]
temp =0
len(A)
for i in range(len(A)):    
    for j in range(10):
        if A[i] in B[j]:
            temp += j
        else :
            pass
print(temp+len(A))
