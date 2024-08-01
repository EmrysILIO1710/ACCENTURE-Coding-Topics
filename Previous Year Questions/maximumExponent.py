# https://prepinsta.com/accenture/coding/ Question 13

def countExponents(n):
    count = 0
    while n % 2 == 0 and n != 0:
        count += 1
        n //= 2
    return count

def MaxExponents(a , b):
    maximum, num = 0, 0
    for i in range(a, b + 1):
        if countExponents(i) > maximum:
            maximum = countExponents(i)
            num = i
    return num

a = int(input())
b = int(input())
print(MaxExponents(a, b))