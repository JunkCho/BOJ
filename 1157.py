A = input()
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alpha2 = [0 for j in range(26)]
alpha2
a = A.lower()
count =0
for i in range(26):
    for k in range(len(A)):
        if a[k] == alpha[i]:
            alpha2[i] += 1
        else :
            pass
for j in range(26):
    if alpha2[j] == max(alpha2):
        count += 1
if count >= 2:
    print('?')
else :
    for l in range(26):
        if alpha2[l] == max(alpha2):
            print(alpha[l].upper())
