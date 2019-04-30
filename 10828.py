N = int(input())
i=0
stack = []
top =-1
for i in range(N):
    O1 = input()
    if O1 == 'top':
        if (top != -1):
            print(int(stack[-1]))
        else : print(-1)
    elif O1 == 'size':
        if (top != -1):
            print(top+1)
        else : print(0)
    elif O1 == 'empty':
        if (top == -1):
            print(1)
        else: print(0)
    elif O1 == 'pop':
        if (top == -1):
            print(-1)
        else :
            p =stack.pop()
            top -= 1
            print(p)
    else:
        if(O1[4] == ' '):
            stack.append(O1[5:])
            top += 1
