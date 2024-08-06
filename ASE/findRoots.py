#find the roots a given quadratic eqn from the coefficients given

def findRoots(a, b, c):
    x1 = (- b + (b ** 2 - ( 4 * a * c)) ** (1 / 2)) / (2 * a)
    x2 = (- b - (b ** 2 - ( 4 * a * c)) ** (1 / 2)) / (2 * a)
    return [round(x1, 3), round(x2, 3)]

a = float(input())
b = float(input())
c = float(input())
print(findRoots(a, b, c))