A = int(input())
temp =0
if A <=99:
    print(A)
elif A>=1000:
    print(144)
else :
    for i in range(100,A+1): 
        if (i//100- ((i-100*(i//100))//10))== (i-100*(i//100))//10 - ((i-100*(i//100))-(10*((i-100*(i//100))//10))):
            temp += 1
    print(temp+99) 
