# https://prepinsta.com/accenture/coding/ Question 5

def differenceofSum(n, m):
    sum1 = 0
    sum2 = 0
    for i in range(m + 1):
        if i % n == 0:
            sum1 += i
        else:
            sum2 += i
    return abs(sum2 - sum1)
n = int(input())
m = int(input())
print(differenceofSum(n, m))