# given an array of integers, return a string stating if the elemnt in array is odd or even

def oddEven(arr):
    res = ""
    for i in arr:
        if i % 2:
            res += "Odd"
        else:
            res += "Even"
    return res

arr = list(map(int, input().split()))
print(oddEven(arr))