#remove duplicates from an array preserving the order

lst = list(map(int, input().split()))
unique_elements = []
for i in lst:
    if i not in unique_elements:
        unique_elements.append(i)
print(unique_elements)