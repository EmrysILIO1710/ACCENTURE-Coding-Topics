# Doug is fond of change, every now and then he tries to do new things. 
# This time, he caught up with a rod comprising of negative (N) and positive (P) charges. 
# He is asked to calculate the maximum net electrostatic field possible in the region due to the rod.

# Note: Assume Electrostatic Field = Total charge * 100

# Input specification:
# Input 1: Integer array denoting the magnitude of each charge.
# Input 2: String denoting nature of each charge ith represents a sign of charge at ith entry represents a sign of charge at ith location in input1
# Input 3: No of charges it holds (length of input1)

# Output Specification:
# Return the next maximum electrostatic field possible in the rod.

# Example 1:
# Input 1: {4,3,5}
# Input 2: PNP
# Input 3: 3

# Output: 600


def maxField(arr, s, n):
    net_charge = 0
    for i in range(n):
        if s[i] == 'P':
            net_charge += arr[i]
        else:
            net_charge -= arr[i]
    return net_charge * 100

arr = list(map(int, input().split()))
s = input()
n = int(input())
print(maxField(arr, s, n))