# reverse a string word-wise

def wordwiseReverse(s):
    s = s.split()
    s = s[::-1]
    s = " ".join(s)
    return s

s = input()
print(wordwiseReverse(s))