# Mr. Professor is a great scientist, but he is not able to find a solution to one problem. 
# There are N straight lines that are not parallel, and no three lines go through the same point. 
# The lines divide the plane into M regions. 
# Write a function to find out the maximum number of such regions he can get on the plane.

def maxDivisions(n):
    return ((n * (n + 1)) // 2) + 1

n = int(input())
print(maxDivisions(n))