#input a number and find the next largest number with the same digits.

s = input()
sl = list(s)
sl.sort()
next_largest = int(s) + 1
while True:
    l = list(str(next_largest))
    l.sort()
    if sl == l:
        break
    next_largest += 1

print(next_largest)