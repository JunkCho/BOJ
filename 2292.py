N = int(input())
i = 0
k = 1
while True:
    k += i * 6
    if k < N:
        i += 1
    else:
        print(i + 1)
        break
