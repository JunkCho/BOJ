A = input()
l = len(A)
temp=0
if (A[0]==' ') and (A[-1] ==' '):
    temp -= 2
elif (A[0]==' ') or (A[-1] ==' '):
    temp -= 1
for B in range(l):
    if A[B] ==' ':
        temp += 1
print(temp+1)
