# Here you are given unbiased dice containing 6 faces. 
# You will be given an output sum which should be obtained by throwing two dice. 
# You need to return the number of all possibilities where the sum on both the dice is equal to the output sum. 
# If there are no possibilities return 0.

def findPossibilities(n):
    count = 0
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == n:
                count += 1
    return count

n = int(input())
print(findPossibilities(n))