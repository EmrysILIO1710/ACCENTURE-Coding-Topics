#write a program that adds up the largest row sum and largest colloumn sum from a m x n matrix

def findSun(m, n, arr):
    arr2 = []
    for i in range(0, len(arr), n):
        arr2.append(arr[i:i + n])
    max_row = 0
    max_coll = 0
    for i in arr2:
        if sum(i) > max_row:
            max_row = sum(i)
    for i in range(m):
        sum_coll = 0
        for j in arr2:
            sum_coll += j[i]
        if sum_coll > max_coll:
            max_coll = sum_coll
    return max_coll + max_row

m = int(input())
n = int(input())
arr = list(map(int, input().split()))
print(findSun(m, n, arr))