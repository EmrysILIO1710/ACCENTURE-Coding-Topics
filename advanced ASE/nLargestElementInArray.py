# find nth largest element in an array

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
if n <= len(lst):
    print(lst[-(n)])
else:
    print("Invalid Input")