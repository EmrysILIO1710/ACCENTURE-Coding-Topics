# The function accepts two strings ‘str1’ and ‘str2’ as its argument. The function needs to return
# the index of the first occurrence of substring ‘str2’ in string ‘str1’ or -1 if the substring is not
# found.

def searchSubstring(str1, str2):
    return str1.find(str2)

str1 = input()
str2 = input()
print(searchSubstring(str1, str2))