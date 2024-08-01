# https://prepinsta.com/accenture/coding/ Question 11

def ReplaceCharacter(str, ch1, ch2):
    res = ""
    for i in str:
        if i == ch1:
            res += ch2
        elif i == ch2:
            res += ch1
        else:
            res += i
    return res

str = input()
ch1 = input()
ch2 = input()
print(ReplaceCharacter(str, ch1, ch2))