# https://prepinsta.com/accenture/coding/ Question 17

def findPallindromes(a, b):
    for i in range(a, b + 1):
        if str(i) == str(i)[::-1]:
            print(i)

a = int(input())
b = int(input())
findPallindromes(a, b)