#find the second largest element in an array

lst = list(map(int, input().split()))
lst.sort()
print(lst[-2])