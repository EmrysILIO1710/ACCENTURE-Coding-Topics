# The function accepts a positive integer array ‘n’ and position of the bit to be turned off ‘k’. 
# Implement the function to turn off the kth bit of the binary representation of ‘n’ and 
# return decimal equivalent of the obtained number. Consider position of ‘k’ according to “little Endian” notation 
# (i.e. right to left).

# Assumptions:

# k > 0
# The number of bits of the binary representation of ‘n’ is >= k
# Note:
# When counting the bits from right to left, start counting from 1. Return ‘n’, if kth bit is already off.

# Example:
# Input:
# n: 19
# k: 2

# Output: 17

# Explanation:
# n: 19
# Binary Representation of n : 10011
# k: 2
# Binary Representation of number after turning off kth bit: 10001
# return Value: 17

def turnOffBit(n, k):
    n = bin(n)[2:]
    n = list(n)
    n[-k] = '0'
    return int(''.join(n), 2)
    
n = int(input())
k = int(input())
print(turnOffBit(n, k))