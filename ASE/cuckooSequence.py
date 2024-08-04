def cuckoo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return 1 * cuckoo(n - 1) + 2 * cuckoo(n - 2) + 3
    
n = int(input())
print(cuckoo(n))