def findSum(arr):
    arr.sort(reverse = True)
    sum = 0
    for i in range(len(arr) - 1):
        sum += (arr[i] - arr[i + 1])
    return sum

arr = list(map(int, input().split()))
print(findSum(arr))