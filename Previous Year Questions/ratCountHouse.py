# https://prepinsta.com/accenture/coding/ Question 1

def countHouse(r, unit, n, arr):
    if n == 0:
        return -1
    total = r * unit
    i = 0
    for i in range(n):
        if sum(arr[:i + 1]) >= total:
            return i + 1
    return 0
    
r = int(input())
unit = int(input())
n = int(input())
arr = list(map(int, input().split()))
print(countHouse(r, unit, n, arr))