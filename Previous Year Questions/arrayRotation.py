# The function accepts an integer array ‘arr’ of size ‘n’ and an integer ‘d’ as its argument. The
# function needs to rotate the array ‘arr’ by ‘d’ positions to the right. The rotation should be done in
# place, without using any additional memory.
# Example:

# Input:
# n: 5
# arr: 1 2 3 4 5
# d: 3
# Output:
# 3 4 5 1 2

def rotateArray(n, arr, d):
    while d >= 1:
        temp = arr[0]
        for i in range(1, n):
            temp, arr[i] = arr[i], temp
        arr[0] = temp
        d -= 1
    return arr

n = int(input())
arr = list(map(int, input().split()))
d = int(input())
print(rotateArray(n, arr, d))