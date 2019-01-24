A = int(input())
i = 0
B = [0,0]
B[0] = A%10*10 + (A//10 + A%10)%10
while A != B[i]:    
    B[i+1] = B[i]%10*10 + (B[i]//10 + B[i]%10)%10
    B.append(B[i])
    i += 1
print(i+1)
