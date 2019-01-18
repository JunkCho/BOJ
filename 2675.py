A = int(input())
for i in range(A):
    a, b= map(str, input().split())
    c = list(map(str, list(b)))        
    for j in range(len(b)):
        for k in range(int(a)):
            print(c[j], end='')
    print('')
