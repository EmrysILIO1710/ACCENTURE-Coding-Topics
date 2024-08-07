# find the longest pallindrome word from input string

def longestPalindrome(s):
    lst = []
    for i in s.split():
        if i == i[::-1]:
            lst.append(i)
    lst.sort(key = len)
    return lst[-1]

s = input()
print(longestPalindrome(s))