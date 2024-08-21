# you are given a string s and your task is to find and return the count of permutations formed by fixing the positions 
# of the vowels present in the string.

def permutations(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    if len(s) == count:
        return 0
    res = 1
    for i in range(1, len(s) - count + 1):
        res *= i
    return res

s = input()
print(permutations(s))