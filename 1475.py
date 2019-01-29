A = input()
N = ['0','1','2','3','4','5','6','7','8','9']
count = [0 for z in range(10)]
count2 =0
for i in range(len(A)):
    for j in range(10):
        if A[i] == N[j]:
            count[j] += 1
        else : pass
count
max(count)
for k in range(10):
    if count[k] == max(count):
        count2 += 1
count2
if count[9] != max(count):
    print(max(count))
elif (count[9] == max(count))& count2 <=1:
    if max(count) % 2 == 0:
        print(int(max(count)/2))
    elif max(count) % 2 == 1:
        print(int((max(count)+1)/2))
elif count[9] == max(count) & count2 >= 2 :
    print(max(count))
