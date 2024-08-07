# input: 1 2 4 -2 3
# output: (1 + 2 + 4), (3)
#         7

def findMax(arr):
    maximum = 0
    s = 0
    for i in arr:
        if i >= 0:
            s += i
        else:
            maximum = max(s, maximum)
            s = 0
            continue
    return max(maximum, s)

arr = list(map(int, input().split()))
print(findMax(arr))