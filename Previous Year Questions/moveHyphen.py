# https://prepinsta.com/accenture/coding/ Question 9

def moveHyphen(str, n):
    if n == 0:
        return ""
    s = str.split('-')
    s = "".join(s)
    return '-' * str.count('-') + s

n = int(input())
str = input()
print(moveHyphen(str, n))