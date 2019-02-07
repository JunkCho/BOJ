import math
N = int(input())
D = 9-12*(1-N)
x1 = (3 + math.sqrt(D)) / 6
if N == 1:
    print(1)
else:
    print(int(x1-0.00001)+1)
