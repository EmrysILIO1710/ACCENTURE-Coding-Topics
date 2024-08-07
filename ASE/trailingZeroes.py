# find the no. of zeroes at the end of the given integer input

def countZeroes(n):
    count = 0
    while n > 0:
        if n % 10:
            return count
        count += 1
        n /= 10
    
n = int(input())
print(countZeroes(n))