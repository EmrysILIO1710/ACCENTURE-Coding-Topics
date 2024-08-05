# print frequency of each charecter in alphabettical order

def getFrequency(s):
    unique_chars = list(set(s))
    unique_chars.sort()
    res = ""
    for i in unique_chars:
        res += i + str(s.count(i))
    return res

s = input()
print(getFrequency(s))