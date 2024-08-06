# Largest Sub Array

# Given an array containing only 0’s and 1’s, Find the largest subarray containing an equal number of 0s and 1s.

# Input specification:
# Input 1: The length of an array.
# Input 2: Array containing 0s and 1s.

# Output Specification:
# Return the length of the largest sub-array containing equal no. of 0s and 1s.

# Example 1:
# Input 1: 4
# Input 2: {1,1,0,1}

# Output: 2
# Explanation:
# The largest possible array here would be of length 2 as there should be an equal number of 0 and 1 in it. 
# The starting index and ending index of the largest subarray is 1 and 2. Hence the output is 2.

# Example 2:
# Input 1: 5
# Input 2: {1,1,1,1,1}

# Output: 0
# Explanation:
# In the above example, there are no 0s in the array. Hence the output is 0.

def largestLength(arr, n):
    length = 0
    for i in range(n):
        for j in range(i, n):
            if arr[i:j + 1].count(0) == arr[i:j + 1].count(1):
                if len(arr[i:j + 1]) > length:
                    length = len(arr[i:j + 1])
    return length

n = int(input())
arr = list(map(int, input().split()))
print(largestLength(arr, n))