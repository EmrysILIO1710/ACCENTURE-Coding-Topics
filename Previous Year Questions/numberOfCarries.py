# https://prepinsta.com/accenture/coding/ Question 10

def NumberOfCarries(num1 , num2):
    carry = 0
    count = 0
    l = max(len(str(num1)), len(str(num2)))
    for _ in range(0, l):
        sum = num1 % 10  + num2 % 10 + carry
        if sum > 9:
            carry = sum // 10
            count += 1
        num1 //= 10
        num2 //= 10
    return count

num1 = int(input())
num2 = int(input())
print(NumberOfCarries(num1, num2))