# My Answer
inputNumber = int(input('Type a number (min: 0/ max: 10): '))
lessonList = [1, 5, 8, 3]

result = inputNumber in lessonList
print(result)

print()

# Solution


def is_group_member(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False


print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))
