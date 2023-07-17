# My answer
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

resultList = []

for color1 in color_list_1:
    if color1 in color_list_2:
        pass
    else:
        resultList.append(color1)

print(resultList)

print()

# Solution
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("Original set elements:")
print(color_list_1)
print(color_list_2)
print("\nDifferenct of color_list_1 and color_list_2:")
print(color_list_1.difference(color_list_2))
print("\nDifferenct of color_list_2 and color_list_1:")
print(color_list_2.difference(color_list_1))
