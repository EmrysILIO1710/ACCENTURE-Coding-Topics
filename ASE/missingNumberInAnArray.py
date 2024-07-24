#given a array of consecutive integers, find the missing element

lst = list(map(int, input().split()))
lst.sort()
flag = 1
diff = min(lst[1] - lst[0], lst[2] - lst[1])
for i in range(len(lst) - 1):
    if lst[i + 1] - lst[i] != diff:
        print(lst[i] + diff)
        flag = 0
        break
if flag:
    print(-1)

#1 2 3 4 5 6 8 9
#3 4 6 2 8 5 9 1
#1 3 5 9
#a[1] - a[0], a[2] - a[1]