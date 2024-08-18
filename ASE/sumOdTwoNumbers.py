# Given an array of integers and an integer sum, find a pair of numbers (a, b) in the array where a
# + b = sum.

def findPair(arr, sum):
    seen = set()
    for num in arr:
        target = sum - num
        if target in seen:
            return [num, target]
        seen.add(num)
    return -1

arr = list(map(int, input().split()))
sum = int(input())
print(findPair(arr, sum))