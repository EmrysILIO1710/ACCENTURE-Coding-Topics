# https://prepinsta.com/accenture/coding/ Question 6

def LargeSmallSum(arr):
    arr.sort()
    l = len(arr)
    if l <= 3:
        return 0
    if l % 2 == 0:
        return arr[3] + arr[-4]
    else:
        return arr[3] + arr[-3]
    
arr = list(map(int, input().split()))
print(LargeSmallSum(arr))