#to check if a given string is a pallindrome

s = input()
if s == s[::-1]:
    print("yes")
else:
    print("no")