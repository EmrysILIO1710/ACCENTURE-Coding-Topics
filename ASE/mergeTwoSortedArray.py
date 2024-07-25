#merge two sorted array into one single sorted array

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
lst1.sort()
lst2.sort()
lst1.extend(lst2)
lst1.sort()
print(lst1)