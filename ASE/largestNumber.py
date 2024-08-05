# The function accepts an integer array ‘arr’ of length ‘size’ as the argument. 
# Implement the function to find and return the maximum number that can be formed by any 
# permutation or arrangement of the digits obtained from all the numbers present in the array. 
# You have to return the number formed as a string. Note: You may need to rearrange the digits of the numbers to form the maximum number.

# Example:
# Input: 34 79 58 64

# Output: 98765443

# Explanation:
# All digits from all the numbers of the array are 3,4,7,9,5,8,6,4. 
# Maximum number obtained after rearranging all these digits gives 98765443.

# Sample input:
# 21 90 23

# Sample Output:
# 932210

def largestNumber(arr):
    s = ""
    for i in arr:
        s += str(i)
    s = sorted(s)
    return int(''.join(s)[::-1])

arr = list(map(int, input().split()))
print(largestNumber(arr))