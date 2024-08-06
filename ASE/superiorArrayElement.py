# Superior Array Element

# In an array, a superior element is one that is greater than all elements to its right. 
# The rightmost element will always be considered as a superior element.

# Here, the function accepts an integer array ‘arr’ and its length ‘n’. 
# Implement the function to find and return the number of superior elements in the array ‘arr’.

# Assumptions:

# n > 0
# Array index starts from 0.
# Example 1:
# Input 1: 7 9 5 2 8 7

# Output: 3
# Explanation:
# 9 is greater than all the elements to its right, 8 is greater than the element to its right, and 7 is the rightmost element. 
# Hence, a total of 3 superior elements.

# Sample Input:
# 2 8 9 7 4 2

# Sample Output:
# 4

def findSuperiorCount(arr):
    count = 1
    for i in range(len(arr) - 1):
        if arr[i] > max(arr[i + 1:]):
            count += 1
    return count

arr = list(map(int, input().split()))
print(findSuperiorCount(arr))