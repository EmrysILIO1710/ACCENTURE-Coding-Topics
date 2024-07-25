#find length of the longest substring without repeating charecters

st = input()
longest_substr = ""
for i in range(len(st)):
    temp = ""
    for j in range(i, len(st)):
        if st[i:j + 1].count(st[j]) == 1:
            temp += st[j]
        else:
            break
    if len(temp) > len(longest_substr):
        longest_substr = temp
print(f"{longest_substr} : {len(longest_substr)}")