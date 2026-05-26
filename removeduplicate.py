lst = [1, 2, 3, 2, 4, 1, 5]

result = []

for i in lst:
    if i not in result:
        result.append(i)

print("List after removing duplicates:", result)