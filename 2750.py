A = int(input())
N=[0 for j in range(A)]
for i in range(A):
    N[i] = int(input())
N.sort()
for k in range(A):
    print(int(N[k]))
