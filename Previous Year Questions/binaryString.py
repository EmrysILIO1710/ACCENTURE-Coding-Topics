# https://prepinsta.com/accenture/coding/ Question 2

def OperationsBinaryString(str):
    if len(str) == 0:
        return -1
    res = int(str[0])
    for i in range(1, len(str) - 1, 2):
        if str[i] == 'A':
            res = res & int(str[i + 1])
        elif str[i] == 'B':
            res = res | int(str[i + 1])
        else:
            res = res ^ int(str[i + 1])
    return res

str=input()
print(OperationsBinaryString(str))