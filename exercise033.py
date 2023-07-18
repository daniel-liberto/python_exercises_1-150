# My answer
inputList = input(
    'Type three numbers separated by comma ex 3,10,4: ').split(',')


def sum(numList):
    aux = 0
    for num in numList:
        if num.isdigit():
            num = int(num.strip())  # just removing whitespaces and cast int
            if num == aux:
                aux = 0
                break
            else:
                aux += num
        else:
            print('\nERROR: Use a valid integer number')
            quit()
    return aux


print(
    f'\nThe sum of the numbers "{inputList[0]}", "{inputList[1]}", "{inputList[2]}" is: {sum(inputList)}')

print()

# Solution


def sum_three(x, y, z):
    if x == y or y == z or x == z:
        sum = 0
    else:
        sum = x + y + z
    return sum


print(sum_three(2, 1, 2))
print(sum_three(3, 2, 2))
print(sum_three(2, 2, 2))
print(sum_three(1, 2, 3))
