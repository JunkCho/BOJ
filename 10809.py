A = input()
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def isnum(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

for i in range(26):
    for k in range(len(A)):
        if A[k] == alpha[i]:
            alpha[i] = k
        else :
            pass

for j in range(26):
    if isnum(alpha[j]) == False:
        alpha[j] = -1
    print(alpha[j] , end =(' '))
