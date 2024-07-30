# https://prepinsta.com/accenture/coding/ Question 4

def findCount(n, arr, num, diff):
    count = 0
    for i in arr:
        if abs(num - i) <= diff:
            count += 1
    if count:
        return count
    else: 
        return -1

n=int(input())
arr=list(map(int,input().split()))
num=int(input())
diff=int(input())
print(findCount(n, arr, num, diff))