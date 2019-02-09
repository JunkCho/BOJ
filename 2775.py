for _ in range(int(input())):
    k = int(input())
    n = int(input())
    room = [[0 for x in range(n)] for y in range(k+1)]
    for j in range(n):
        room[0][j] = j + 1
    for j in range(1, k+1):
        for i in range(n):
            s = 0
            if i==0:
                room[j][i] = 1
            else:
                for x in range(i + 1):
                    s += room[j-1][x]
                room[j][i] = s
    print(room[k][n-1])
