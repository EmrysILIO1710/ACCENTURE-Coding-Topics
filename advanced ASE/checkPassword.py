# https://prepinsta.com/accenture/coding/ Question 3

def CheckPassword(s,n):
    checker1 = 0
    checker2 = 0
    checker3 = 1
    if len(s) < 4 and s[0].isnumeric():
        return 0
    for i in s:
        if i.isnumeric():
            checker1 = 1
        elif i.isupper():
            checker2 = 1
        elif i == ' ' or i == '/':
            checker3 = 0
    return checker1 and checker2 and checker3

s=input()
a=len(s)
print(CheckPassword(s,a))