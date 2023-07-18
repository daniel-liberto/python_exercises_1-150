# My answer
num1 = int(input('Type first number: '))
num2 = int(input('Type second number: '))


def sumNumber(n1, n2):
    result = n1 + n2
    if result >= 15 and result <= 20:
        result = 20
    return result


print(f'\nThe sum of the numbers given is: {sumNumber(num1, num2)}')

print()

# Solution


def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum


print(sum(10, 6))
print(sum(10, 2))
print(sum(10, 12))
