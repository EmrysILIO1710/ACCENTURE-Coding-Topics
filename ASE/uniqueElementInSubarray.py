# given an array and a integer n, find the number of elemnts with frequency 1 in subarrays of size n.

def countUniqueElements(arr, n):
    count = 0
    for i in range(len(arr) - n + 1):
        for j in arr[i: i + n]:
            if arr[i: i + n].count(j) == 1:
                count += 1
    return count

n = int(input())
arr = list(map(int, input().split()))
print(countUniqueElements(arr, n))