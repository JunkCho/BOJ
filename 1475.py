import sys
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
for k in range(10):
    if count[k] == max(count):
        count2 += 1
count2
if count[0] == max(count) or count[1] == max(count) or count[2] == max(count) or count[3] == max(count) or count[4] == max(count) or count[5] == max(count) or count[7] == max(count) or count[8] == max(count):
    print(max(count))
    sys.exit()

if count[9] < max(count) and count[6] < max(count) and count2 >= 2:
    print(max(count))
elif count[6] == max(count) or count[9] == max(count):
    if (count[6] + count[9]) % 2 == 1:
        print(int(((count[6] + count[9])+1)/2))
    elif (count[6] + count[9]) % 2 == 0:
        print(int((count[6] + count[9])/2))
