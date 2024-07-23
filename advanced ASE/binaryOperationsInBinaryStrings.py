# program to perform binary operations like AND OR XOR on binary strings

n1 = input()
n2 = input()
# n1 = int(n1)
# n2 = int(n2)
l = max(len(n1), len(n2))
n1 = n1.rjust(l, "0")
n2 = n2.rjust(l, "0")
res_and = ""
res_or = ""
res_xor = ""
for i in range(l):
    res_and += str(int(n1[i]) & int(n2[i]))
    res_or += str(int(n1[i]) | int(n2[i]))
    res_xor += str(int(n1[i]) ^ int(n2[i]))
print(f"AND: {res_and}")
print(f"OR: {res_or}")
print(f"XOR: {res_xor}")