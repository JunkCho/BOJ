import math
N = int(input())
B = math.ceil(((N%5)/3))
print('%d' %(B + N/5))
