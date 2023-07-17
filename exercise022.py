# My answer
inputList = input(
    'Type 5 numbers separated by comma. ex:(4,21,35,10,2): ').split(',')
counter = 0

for number in inputList:
    if int(number) == 4:
        counter += 1
    else:
        pass

print(f'The list {inputList} have the number 4 appeared: {counter} times.')

print()

# Solution


def list_count_4(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1

    return count


print(list_count_4([1, 4, 6, 7, 4]))
print(list_count_4([1, 4, 6, 4, 7, 4]))
