# find the total no. of coprime pairs from 1 to given input
# input = 16
# output = 8
# explanation: (1, 16) (3, 16) (5, 16) (7, 16) (9, 16) (11, 16) (13, 16) (15, 16)
# coprime numbers are numbers that have only one common factor, that is 1

def checkCoprime(a, b):
    for i in range(2, a + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True

def countCoprime(n):
    count = 0
    for i in range(1, n):
        if checkCoprime(i, n):
            count += 1
    return count

n = int(input())
print(countCoprime(n))