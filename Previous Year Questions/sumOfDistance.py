# https://prepinsta.com/accenture/coding/ Question 18

import math

def findSum(x1, y1, x2, y2, x3, y3):
    first_diff = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))
    second_diff = math.sqrt(math.pow(x3-x2, 2) + math.pow(y3-y2, 2))
    third_diff = math.sqrt(math.pow(x3-x1, 2) + math.pow(y3-y1, 2))
    return(round(first_diff,2) + round(second_diff,2) + round(third_diff,2))

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
print(findSum(x1, y1, x2, y2, x3, y3))