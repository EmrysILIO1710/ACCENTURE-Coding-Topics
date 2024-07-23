# find the count of combinations of elements in a list that is equal to the given sum

def find_combinations(index, current_sum, combination):
    global count
    if current_sum == target_sum:
        count += 1
        # print(*combination)
        return
    if current_sum > target_sum or index >= len(lst):
        return
    for i in range(index, len(lst)):
        find_combinations(i + 1, current_sum + lst[i], combination + [lst[i]])

lst = list(map(int, input().split()))
target_sum = int(input())
count = 0

find_combinations(0, 0, [])
print(count)