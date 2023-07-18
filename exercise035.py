# My answer
num1 = int(input('Type first number: '))
num2 = int(input('Type second number: '))


def sumNumber(n1, n2):
    if n1 == n2 or abs(n1 - n2) == 5 or n1 + n2 == 5:
        return True
    else:
        return False


print(f'\nThe sum of the numbers given is: {sumNumber(num1, num2)}')

print()

# Solution


def test_number5(x, y):
    if x == y or abs(x-y) == 5 or (x+y) == 5:
        return True
    else:
        return False


print(test_number5(7, 2))
print(test_number5(3, 2))
print(test_number5(2, 2))
print(test_number5(7, 3))
print(test_number5(27, 53))
