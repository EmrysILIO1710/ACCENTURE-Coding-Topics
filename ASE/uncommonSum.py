# find the sum of uncommon elements in two arrays. return -1 if both the arrays are null.

def findSum(arr1, arr2):
    if len(arr1) == 0 and len(arr2) == 0:
        return -1
    arr1 = set(arr1) ^ set(arr2)
    return sum(arr1)

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(findSum(arr1, arr2))