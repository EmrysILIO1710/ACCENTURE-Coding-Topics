# write a program to find nth primne number

def isPrime(num):
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True

def nthPrime(n):
    count = 0
    num = 1
    while count != n:
        num += 1
        if isPrime(num):
            count += 1
    return num
        
n = int(input())
print(nthPrime(n))