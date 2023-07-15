# My answer
print('Type 3 integers numbers to sum them')
num1 = int(input('\nType number 1: '))
num2 = int(input('Type number 2: '))
num3 = int(input('Type number 3: '))
originalValue = num1 + num2 + num3

if num1 == num2 == num3:
    print(
        f'\nThe numbers are equal, so it will return three times of the sum value with a new value of: {(num1 + num2 + num3) * 3}')
    print(f'Original value without penalty: {originalValue}')
else:
    print(
        f'\nThe sum of the numbers "{num1}", "{num2}" and "{num3}" are: {originalValue}')

print()

# Solution


def sum_thrice(x, y, z):

    sum = x + y + z

    if x == y == z:
        sum = sum * 3
    return sum


print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))
