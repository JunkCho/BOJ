A = input()
B = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
l = len(A)
for i in range(len(A)-1):
    if A[i] + A[i+1] in B:
        l -= 1
    else :
        pass
for j in range(len(A)-2):
    if A[j] + A[j+1] + A[j+2] in B:
        l -= 1
    else :
        pass
print(l)      
