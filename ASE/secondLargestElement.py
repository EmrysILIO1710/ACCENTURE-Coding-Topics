#find the second largest element in an array

lst = list(map(int, input().split()))
lst = set(lst)
lst = list(lst)
lst.sort()
if lst[-2]:
    print(lst[-2])
else:
    print("-1")