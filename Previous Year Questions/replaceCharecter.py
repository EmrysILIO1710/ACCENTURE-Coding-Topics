# https://prepinsta.com/accenture/coding/ Question 11

def ReplaceCharacter(str, ch1, ch2):
    res = ""
    res = str.replace(ch1, "*").replace(ch2, ch1).replace("*", ch2)
    return res

str = input()
ch1 = input()
ch2 = input()
print(ReplaceCharacter(str, ch1, ch2))