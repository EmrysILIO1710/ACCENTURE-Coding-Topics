#count occurance of each element in an array

lst = list(map(int, input().split()))
unique_elements = set(lst)
for i in unique_elements:
    print(f"{i} : {lst.count(i)}")
