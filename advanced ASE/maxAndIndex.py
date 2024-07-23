# to find largest element and it's index in an array

lst = list(map(int, input().split()))
duplicate = lst[:]
# The lst is getting sorted because the assignment duplicate = lst does not create a new list; instead, it creates a new reference to the same list object. Therefore, when duplicate.sort() is called, it sorts the original list lst in-place due to both duplicate and lst referring to the same list object in memory. To avoid this and keep the original list lst unsorted, you should create a copy of the list when assigning it to duplicate. This can be done using duplicate = lst[:] or duplicate = lst.copy().
duplicate.sort()
max = duplicate[-1]
print(f"{max} present at {lst.index(max)}")
print(lst)