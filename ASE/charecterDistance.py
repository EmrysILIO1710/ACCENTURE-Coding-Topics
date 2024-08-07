# The function accepts two characters ‘ch1’ and ‘ch2’ as the argument. 
# ‘ch1’ and ‘ch2’ are alphabetical letters. 
# Implement the function to find and return the next letter so that distance between ch1 and ch2. 
# While counting distance if you exceed the letter ‘z’ then count the remaining distance starting from the letter ‘a’.

# Distance between two letters in the number of letters between them.

# Assumptions:
# All input and output characters are lower case alphabets.

# Example 1:
# Input 1: c
# Input 2: g

# Output: k
# Explanation:
# The distance between the letter ‘c’ and ‘g’ is 3 (d,e,f). The next letter with distance 3 from letter ‘g’ is ‘k’. 
# Thus the output is k.

# Sample Input:
# Input 1: r
# Input 2: l

# Sample Output:
# f

def nextChar(c1, c2):
    l = ord(c2) - ord(c1)
    if ord(c2) + l <= 122:
        return chr(ord(c2) + l)
    return chr(96 + ord(c2) + l - 122)

c1 = input()
c2 = input()
print(nextChar(c1, c2))