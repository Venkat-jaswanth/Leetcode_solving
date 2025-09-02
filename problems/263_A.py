a = [[0]*5 for _ in range(5)]

for i in range(5):
    a[i] = list(map(int, input().split(" ")))
    for j in range(5):
        if a[i][j] == 1:
            x, y = i, j

print(abs(x-2) + abs(y-2))