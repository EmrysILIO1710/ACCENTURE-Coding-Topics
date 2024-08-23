# swap the values in the even positions of the binary representation of a number with the values at odd position

def nextDay(n):
    binary = bin(n)[2:]
    if len(binary) % 2:
        binary = '0' + binary
    binary = list(binary)
    for i in range(0, len(binary), 2):
        binary[i], binary[i + 1] = binary[i + 1], binary[i]
    return int(''.join(binary), 2)

n = int(input())
print(nextDay(n))