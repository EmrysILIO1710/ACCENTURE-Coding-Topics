# https://prepinsta.com/accenture/coding/ Question 20

def FindAutoCount(n):
    if len(n) == 0:
        return 0
    for i in range(len(n)):
        if int(n[i]) != n.count(str(i)):
            return 0
    n2 = set(list(n))
    return len(n2)

n = input()
print(FindAutoCount(n))