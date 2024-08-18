# The function accepts an integer array ‘arr’ of size ‘n’ as its argument. The function needs to
# return the index of an equilibrium point in the array, where the sum of elements on the left of the
# index is equal to the sum of elements on the right of the index. If no equilibrium point exists, the
# function should return -1.

def findEquilibriumPoint(arr, n):
    for i in range(n):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    return -1

n = int(input())
arr = list(map(int, input().split()))
print(findEquilibriumPoint(arr, n))