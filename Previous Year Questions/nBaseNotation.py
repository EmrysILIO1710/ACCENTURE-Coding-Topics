# https://prepinsta.com/accenture/coding/ Question 8

def convert(n, num):
    res = ""
    while num > 0:
        rem = num % n
        if rem > 9:
            res = chr(55 + rem) + res
            # print(rem)
        else: 
            res = str(rem) + res
        num //= n
    return res

n = int(input())
num = int(input())
print(convert(n, num))