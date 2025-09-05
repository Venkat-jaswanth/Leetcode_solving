def nestedRange(ranges=[[1, 6], [2, 4], [4, 8], [3, 6]]):
    # Initialize result to hold information about each range
    contains = [0] * len(ranges)  # Tracks if a range contains another range
    contained_by = [0] * len(ranges)  # Tracks if a range is contained by another range

    for i in range(len(ranges)):
        for j in range(len(ranges)):
            if i != j:
                # Check if range[i] contains range[j]
                if ranges[i][0] <= ranges[j][0] and ranges[i][1] >= ranges[j][1]:
                    contains[i] = 1
                # Check if range[i] is contained by range[j]
                if ranges[i][0] >= ranges[j][0] and ranges[i][1] <= ranges[j][1]:
                    contained_by[i] = 1

    # Combine results into a list of dictionaries for better readability
    # # 1 0 0 0 0 1 0 1
    result= [contains, contained_by]
    for j in range(2):
        for i in range(len(ranges)):
            print(result[j][i] ,end=" " if i != len(ranges)-1 else "\n")
            


n = int(input())
arr = []
for i in range(n):
    a = list(map(int, input().strip().split()))
    x = a[0]
    y = a[1]
    arr.append([x, y])
nestedRange(arr)

