# given an array of length n, find the sum of elements in even positions after reversing the array.

def findSum(a, n):
    if n % 2:
        start = 0
    else:
        start = 1
    sum = 0
    for i in range(start, n, 2):
        sum += a[i]
    return sum

n = int(input())
a = list(map(int, input().split()))
print(findSum(a, n))