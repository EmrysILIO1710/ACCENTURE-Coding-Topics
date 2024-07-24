#find the common elements in two given arrays

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
common_elements = []
for i in lst1:
    if i in lst2 and i not in common_elements:
        common_elements.append(i)
print(*common_elements)